from django.shortcuts import render
from django.http  import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from learn_api.models import Snippet
from learn_api.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
    """
    An HttpPresponse that renders its content into json
    """
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

# @csrf_exempt 注解来标识一个视图可以被跨域访问
@csrf_exempt
def snippet_list(request):
    """
    列出所有的code snippet,或者创建一个新的snippet
    """
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializer  = SnippetSerializer(snippet,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)

@csrf_exempt
def snippet_detail(request,pk):  #pk 代表主键
    """
    获取，更新或者删除一个 code snippet
    """
    print(request.method,"test")
    try:
        snippet = Snippet.objects.get(pk=pk)  #根据主键查找对应的信息
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data  = JSONParser().parse(request)  # JSONParser().parse(request)  反序列化
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


































