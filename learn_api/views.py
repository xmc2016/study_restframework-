from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



































