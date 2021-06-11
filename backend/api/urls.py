from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .api import ProjectInfoViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectInfoViewSet)

urlpatterns = router.urls