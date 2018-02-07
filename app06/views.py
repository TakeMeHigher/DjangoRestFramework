from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


from app06 import models



class UserSerializers(serializers.Serializer):
    name=serializers.CharField()
    pwd=serializers.CharField()
    group_id=serializers.CharField()
    group=serializers.CharField(source='group.title')


# Create your views here.

class SerView(APIView):
    def get(self,request,*args,**kwargs):
        user_list=models.UserInfo.all()
        ser=UserSerializers(instance=user_list,many=True)
        print(ser.data)
        return Response(ser.data)
