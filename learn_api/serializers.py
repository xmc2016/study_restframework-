# -*- coding: utf-8 -*-
'''
File Name: serializers.py
Author: minchao.xue
mail: minchao.xue@shuyun.com
Created Time: 2020/7/7 17:14
'''
# 用于数据展示,序列化程序

from django.contrib.auth.models import User,Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        mode = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')





