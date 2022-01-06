from django.urls import path
from rest_framework import routers
from school import views

router = routers.DefaultRouter()

router.register('schools', views.SchoolViewSet, basename='school')
router.register('students', views.StudentViewSet)

urlpatterns = router.urls