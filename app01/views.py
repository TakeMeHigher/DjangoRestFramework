import json
import hashlib
import time

from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from app01 import models


# Create your views here.
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        user = models.Userinfo.objects.filter(token=token).first()
        if user:
            return (user.name, user)
        return None
    def authenticate_header(self,request):
        pass


class Mypermission(object):
    message='无权访问'
    def has_permission(self,request,view):
        if request.user:
            print(request.user)
            return True
        return False


class Adminpermission(object):
    message='无权访问'
    def  has_permission(self,request,view):
        if request.user=='ctz':
            return True
        return False


class AuthView(APIView):
    # 设置为空标识不用认证
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        dic = {'code': 1000, 'msg': ''}
        pwd = request.query_params.get('pwd')
        name = request.query_params.get('name')

        user = models.Userinfo.objects.filter(name=name, pwd=pwd).first()
        if not user:
            dic['msg'] = '用户名或密码错误'
            dic['code'] = 1001
            return Response(dic)
        t = time.time()
        key = '%s|%s' % (name, t)
        m = hashlib.md5()
        m.update(key.encode('utf-8'))
        token = m.hexdigest()

        user.token = token
        user.save()
        dic['token'] = token
        dic['msg'] = '登陆成功'
        return Response(dic)


class HostView(APIView):
    '''
    要求:所有人都可以访问
    '''
    authentication_classes=[MyAuthentication,]
    permission_classes = []
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法

        注意：APIView中的dispatch方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')


class Userview(APIView):
    '''
        要求:登录用户可以访问
        '''
    authentication_classes = [MyAuthentication, ]
    permission_classes = [Mypermission,]
    def get(self, request):
        return Response('用户列表')


class Salview(APIView):
    '''
            要求:管理员可以访问
            '''
    authentication_classes = [MyAuthentication, ]
    permission_classes = [Mypermission,Adminpermission, ]
    def get(self, request):
        return Response('薪资列表')

