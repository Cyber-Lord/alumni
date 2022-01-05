from django.urls import path
from rest_framework import routers
from school import views

router = routers.DefaultRouter()

router.register('schools', views.SchoolViewSet, basename='school')

urlpatterns = router.urls