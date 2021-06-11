from .models import ProjectInfo
from rest_framework import viewsets
from .serializers import ProjectInfoSerializer

class ProjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ProjectInfo.objects.filter(show=True)
    serializer_class = ProjectInfoSerializer