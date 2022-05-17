from rest_framework import serializers
from .models import Hero, Todo, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_user', 'is_admin')

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'task', 'completed', 'timestamp', 'updated', 'user')