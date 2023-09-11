from rest_framework import serializers
from todos.models import Todo

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id","title","text",)