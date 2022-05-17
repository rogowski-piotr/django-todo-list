from rest_framework import serializers
from .models import Todo, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_user', 'is_admin')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'content', 'completed', 'user', 'timestamp', 'updated')