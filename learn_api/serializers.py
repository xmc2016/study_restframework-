from rest_framework import  serializers
from learn_api.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    #owner会在创建新的Snippet的时候拥有User的各个属性，那么在API中要让owner显示id还是用户名，
    # 为了提高可读性，答案当然是显示用户名了，所以我们在SnippetSerializer 下面增加一个字段：
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style','owner')


class UserSerializer(serializers.ModelSerializer):

    #因为'snippets' 在用户模型中是一个反向关联关系。在使用 ModelSerializer 类时它默认不会被包含，所以我们需要为它添加一个显式字段。
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields =('id','username','snippets')




# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
#
#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的`Snippet` 实例。
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例
#         """
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.linenos = validated_data.get('linenos',instance.linenos)
#         instance.language = validated_data.get('language',instance.language)
#         instance.style = validated_data.get('style',instance.style)
#         instance.save()
#
#         return instance





















