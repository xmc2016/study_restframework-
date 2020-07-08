from django.shortcuts import render
from django.http  import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def snippet_list(request,format=None):
    """
    列出所有的code snippet,或者创建一个新的snippet
    """
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializer  = SnippetSerializer(snippet,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):  #pk 代表主键
    """
    获取，更新或者删除一个 code snippet
    """
    print(request.method,"test")
    try:
        snippet = Snippet.objects.get(pk=pk)  #根据主键查找对应的信息
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data  = JSONParser().parse(request)  # JSONParser().parse(request)  反序列化
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Response渲染成客户端请求的内容类型。
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


































