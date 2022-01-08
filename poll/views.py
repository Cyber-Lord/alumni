from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PollViewSet(ModelViewSet):
    queryset = 'Hello'
    serializer_class = ModelViewSet
