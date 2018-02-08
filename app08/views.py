from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
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



#基于GenericViewSet
# class UserListView(GenericViewSet):
#     authentication_classes = []
#     permission_classes = []
#
#     pagination_class = P2
#     serializer_class = UserSerializers
#     queryset = models.UserInfo.objects.all()
#     def list(self,request,*args,**kwargs):
#         userlist = models.UserInfo.objects.all()
#         ser=UserSerializers(userlist,many=True)
#         return Response(ser.data)
#
#     def retrieve(self,request,*argsm,**kwargs):
#         user=models.UserInfo.objects.filter(id=kwargs.get('pk')).first()
#         ser=UserSerializers(user,many=False)
#         return Response(ser.data)
#
#     def create(self,request,*args,**kwargs):
#         return Response('post')
#
#
#     def update(self,request,*args,**kwargs):
#         return Response('put')
#
#     def partial_update(self,request,*args,**kwargs):
#         return Response('patch')
#
#     def destroy(self,request,*args,**kwargs):
#         return Response('delete')


class UserListView(ModelViewSet):
    authentication_classes = []
    permission_classes = []



    queryset = models.UserInfo.objects.all()
    serializer_class = UserSerializers
    pagination_class = P2