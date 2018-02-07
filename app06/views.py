from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


from app06 import models

class MyCharFiled(serializers.CharField):
    def to_representation(self,value):
        print(value)
        return {'id':value.pk,'name':value.name}

class UserSerializers(serializers.Serializer):
    name=serializers.CharField()
    pwd=serializers.CharField()
    group_id=serializers.CharField()
    group=serializers.CharField(source='group.title')
    menu=serializers.CharField(source='group.mu.name')
    #role=serializers.CharField(source=('roles.all'))
    #roles=serializers.ListField(child=MyCharFiled(),source='roles.all')
    roles=serializers.SerializerMethodField()

    def get_roles(self,obj):
        roles=obj.roles.all()
        data_list=[]
        for role in roles:
            data_list.append({'id':role.id,'name':role.name})
        return data_list

class UserSerializers1(serializers.ModelSerializer):
    class Meta:
        model=models.UserInfo
        fields='__all__'
        depth=2



# Create your views here.
class SerView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        user_list=models.UserInfo.objects.all()
        ser=UserSerializers1(instance=user_list,many=True,context={'request':request})
        print(ser.data)
        return Response(ser.data)
