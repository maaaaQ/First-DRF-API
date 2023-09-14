from rest_framework import generics
from django.shortcuts import render
from .serializers import WomenSerializer
from .models import Women
from rest_framework import viewsets


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
