from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import BasePagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers


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

class P1(LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 2


class MyResponse(object):
    def __init__(self,data=None,code=1000,errors=None):
        self.data=data
        self.code=code
        self.errors=errors



class UserListView(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self,request,*args,**kwargs):
        res = MyResponse()
        try:
            users=models.UserInfo.objects.all()
            p1 = P1()
            page_list=p1.paginate_queryset(users,request,self)
            ser=UserSerializers(instance=page_list,many=True)
            res.data=ser.data
            res.next=p1.get_next_link()
            res.previous=p1.get_previous_link()
        except Exception:
            res.errors='xxxx出错'
            res.code=1001

        return Response(res.__dict__)
