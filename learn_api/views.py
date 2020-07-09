from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    列出所有的snippets 或者创建一个新的snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return  self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


































