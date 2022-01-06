from django.http import response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from school.serializers import SchoolSerializer, StudentSerializer
from .models import School, Student


class SchoolViewSet(ModelViewSet):
    http_method_names = ['post', 'get']
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer