from doctest import FAIL_FAST
from rest_framework import viewsets
from .serializers import HeroSerializer, TodoSerializer, UserSerializer
from .models import Hero, Todo, User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        # checking user
        # print(request.user)

        # non logged user
        # if request.user.is_anonymous:
        #     print('not logged')
        #     return False

        # checking action (list, retrieve, create ...)
        # print(view.action)

        # checking type of view in request (domain od request)
        if type(view) is TodoView:
            return True if request.user.is_user else False
        
        if type(view) is UserView:
            return True if request.user.is_admin else False
        
        return False


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = (ActionBasedPermission,)

    def list(self, request):
        print('list users')
        queryset = User.objects.all().order_by('username')
        return Response(UserSerializer(queryset, many=True, context={ 'request': request }).data, status=200)

    def destroy(self, request, pk=None):
        print('delete user')
        queryset = User.objects.all().order_by('username')
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(UserSerializer(user, many=False, context={ 'request': request }).data, status=204)

class HeroView(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (ActionBasedPermission,)
    queryset = Todo.objects.all().order_by('task')

    def list(self, request):
        print('list todos')
        queryset = Todo.objects.all().order_by('task').filter(user=request.user.id)
        return Response(TodoSerializer(queryset, many=True, context={ 'request': request }).data, status=200)

    def retrieve(self, request, pk=None):
        print('retrieve todos')
        queryset = Todo.objects.all().order_by('task')
        todo = get_object_or_404(queryset, pk=pk)
        return Response(TodoSerializer(todo, many=False, context={ 'request': request }).data, status=200)

    def update(self, request, pk=None, project_pk=None):
        print('update todos')
        try:
            todo = Todo.objects.all().get(pk=pk)
            todo.completed = True
            todo.save()
            return Response(status=200)
        except:
            return Response(status=204)

@api_view(['GET',])
def check_credentials(request):
    print(request)
    if request.user.is_anonymous:
        return HttpResponse(status=401)
    return Response(UserSerializer(request.user, many=False, context={ 'request': request }).data, status=200)
