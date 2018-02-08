from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination


from app06 import models

class MyCharFiled(serializers.CharField):
    def to_representation(self,value):
        print(value)
        return {'id':value.pk,'name':value.name}

class PasswordValidate(object):
    def __init__(self,val):
        self.val=val

    def __call__(self,value):
        if self.val !=value:
            message='密码必须是%s'%self.val
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass


class UserSerializers(serializers.Serializer):
    name=serializers.CharField()
    pwd=serializers.CharField(error_messages={'required':'密码不能为空'},validators=[PasswordValidate('123'),])
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
        self.dispatch
        user_list=models.UserInfo.objects.all()
        ser=UserSerializers(instance=user_list,many=True,context={'request':request})
        print(ser.data)
        return Response(ser.data)


    def post(self,request,*args,**kwargs):
        ser=UserSerializers(request.data)
        print(request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)
        return Response('Post请求')
