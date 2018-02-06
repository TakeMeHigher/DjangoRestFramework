from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.throttling import SimpleRateThrottle
from rest_framework import exceptions

from app01 import models

# Create your views here.
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_params.get('token')
        user=models.Userinfo.objects.filter(token=token).first()
        if user:
            return (user.name,user)
        return None

class UserPermission(BasePermission):
    message='登录用户才可以访问'
    def has_permission(self, request, view):
        if request.user:
            return True
        return False

class AdminPermission(BasePermission):
    message='管理员才能访问'
    def has_permission(self, request, view):
        if request.user =='ctz':
            return True
        return False

class AnnoThrottle(SimpleRateThrottle):
    scope = 'anno'
    def get_cache_key(self, request, view):
        #如果是匿名用户则执行
        if not request.user:
            return self.get_ident(request)
        #如果不是匿名用户则让他执行
        return None
class UserThrottle(SimpleRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        #当前用户登陆了,并且当前用户不是管理员
        if request.user and request.user!='ctz':
            return self.get_ident(request)
        #如果是匿名用户和管理员 则让他继续执行
        return None

class AdminThrottle(SimpleRateThrottle):
    scope = 'admin'

    def get_cache_key(self, request, view):
        #如果是管理员
        if request.user=='ctz':
            return self.get_ident(request)
        #不是管理员
        return  None