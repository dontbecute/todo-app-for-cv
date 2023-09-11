from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from todos.models import Todo

from .serializers import todoSerializer

class TodoAPIList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer

class TodoAPIDetalis(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = todoSerializer