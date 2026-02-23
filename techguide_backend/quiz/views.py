from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Domain, QuizQuestion, QuizChoice, ChoiceDomainScore
from .serializers import QuizQuestionSerializer


class QuizQuestionsAPIView(APIView):
    def get(self, request):
        questions = QuizQuestion.objects.all().order_by('order')
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class SubmitQuizAPIView(APIView):
    def post(self, request):
        print("RECEIVED DATA:", request.data)
        answers = request.data.get('answers', {})
        print("ANSWERS:", answers)

        if not answers:
            return Response(
                {'error': 'No answers provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calculate score per domain
        domain_scores = {}
        for question_id, choice_id in answers.items():
            try:
                choice = QuizChoice.objects.get(id=int(choice_id))
                score_entries = ChoiceDomainScore.objects.filter(choice=choice)
                for entry in score_entries:
                    domain_id = entry.domain.id
                    if domain_id not in domain_scores:
                        domain_scores[domain_id] = 0
                    domain_scores[domain_id] += entry.score
            except QuizChoice.DoesNotExist:
                continue

        if not domain_scores:
            return Response(
                {'error': 'Could not calculate scores'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get top 3 domains
        max_score = max(domain_scores.values())
        sorted_domains = sorted(
            domain_scores.keys(),
            key=lambda d: domain_scores[d],
            reverse=True
        )[:3]

        results = []
        for domain_id in sorted_domains:
            domain = Domain.objects.get(id=domain_id)
            score = domain_scores[domain_id]
            compatibility = int((score / max_score) * 100)
            results.append({
                'name': domain.name,
                'slug': domain.slug,
                'icon_emoji': domain.icon_emoji,
                'color_hex': domain.color_hex,
                'compatibility': compatibility,
            })

        print("RESULTS:", results)
        return Response({'results': results})