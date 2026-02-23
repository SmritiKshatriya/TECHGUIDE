from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoadmapStep
from .serializers import RoadmapStepSerializer


class RoadmapAPIView(APIView):
    def get(self, request):
        domain = request.query_params.get('domain', None)

        if not domain:
            return Response(
                {'error': 'domain parameter required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        steps = RoadmapStep.objects.filter(
            domain__slug=domain
        ).prefetch_related('resources').order_by('level', 'order')

        serializer = RoadmapStepSerializer(steps, many=True)
        return Response(serializer.data)
