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

class IndexView(APIView):
    '''
    要求,所有用户都能访问，匿名用户5/m,普通用户10/m,管理员不限
    '''
    authentication_classes = [MyAuthentication,]
    permission_classes = []
    throttle_classes = [AnnoThrottle,UserThrottle,AdminThrottle]
    def get(self,request):
        return Response('首页')

    def throttled(self, request, wait):
        class UserInnerThrottled(exceptions.Throttled):
            default_detail = '请求被限制.'
            extra_detail_singular = 'Expected available in {wait} second.'
            extra_detail_plural = '还需要再等待{wait}秒'
        raise UserInnerThrottled(wait)

class UserView(APIView):
    '''
    要求:登录用户能访问,普通用户10/m,管理员20/m
    '''
    authentication_classes = [MyAuthentication,]
    permission_classes = [UserPermission,]
    throttle_classes = [UserThrottle,AdminThrottle]
    def get(self,request):
        return Response('用户界面')

    def permission_denied(self, request, message=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated('无权访问')
        raise exceptions.PermissionDenied(detail=message)


    def throttled(self, request, wait):
        class UserInnerThrottled(exceptions.Throttled):
            default_detail = '请求被限制.'
            extra_detail_singular = 'Expected available in {wait} second.'
            extra_detail_plural = '还需要再等待{wait}秒'
        raise UserInnerThrottled(wait)