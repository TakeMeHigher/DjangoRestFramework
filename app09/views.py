from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from app06 import models
# Create your views here.

class  UserSerializers(serializers.Serializer):
    name=serializers.CharField()
    pwd=serializers.CharField(required=True,error_messages={'required':'密码不能为空'})
    group=serializers.CharField(source='group.title')
    roles=serializers.SerializerMethodField()

    def get_roles(self,obj):
        roles=obj.roles.all()
        roles_list=[]
        for role in roles:
            roles_list.append({'id':role.id,'name':role.name})
        return roles_list



class P2(PageNumberPagination):
    page_size =1
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 2


class UserListView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        users=models.UserInfo.objects.all()
        print(users)
        p2=P2()
        page_list=p2.paginate_queryset(users,request,self)
        ser=UserSerializers(instance=users,many=True)
        response=p2.get_paginated_response(ser.data)

        return response


