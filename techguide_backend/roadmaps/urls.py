from django.urls import path

from .views import RoadmapAPIView

app_name = 'roadmaps'

urlpatterns = [
    path('', RoadmapAPIView.as_view(), name='roadmap'),
]
