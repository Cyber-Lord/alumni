from django.urls import path
from rest_framework import routers

from poll import views

router = routers.DefaultRouter()

router.register('home', views.PollViewSet, basename='home')
urlpatterns = router.urls