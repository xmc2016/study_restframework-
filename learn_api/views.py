from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer ,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from learn_api.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import renderers


@api_view(['GET'])
def api_root(request,format=None):

    #reverse功能来返回完全限定的URL
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self,request,*args ,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)





class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 登录后才能创建，更新和删除代码片段
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#这个perform_create() 可以让用户在通过POST请求创建一个新的Snippet时，
# 在保存新的Snippet数据的时候会把request中的user赋值给Snippet的owner
    def perform_create(self, serializer):
        serializer.save(owner =self.request.user)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


































