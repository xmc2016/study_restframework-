from django.shortcuts import render
from django.http  import  HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from learn_api.serializers import UserSerializer,GroupSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或者编辑的API路径
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# def test_django(request):
#     return HttpResponse('hello world!')

