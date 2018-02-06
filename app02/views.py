from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import exceptions

from app02.utils import MyPermission
#
#
from app01 import models
# # Create your views here.
#
# class MyAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         token=request.query_params.get('token')
#         user=models.Userinfo.objects.filter(token=token).first()
#         if user:
#             return (user.name,user)
#         return None
#
# class MyPermission(object):
#     message = '登录才可以访问'
#     def has_permission(self,request, view):
#         if request.user:
#             return True
#         return False
#
# class AdminPermission(object):
#     message = '会员才可以访问'
#     def has_permission(self,request,view):
#         if request.user=='ctz':
#             return True
#         return False

class Pview(APIView):
    '''
    所有人都可以看
    '''

    permission_classes = []
    def get(self,request):
        return Response('图片列表')
    def post(self,request):
        pass




class Aview(APIView):
    '''
    登录的人可以看
    '''
  #  authentication_classes = [MyAuthentication,]
    permission_classes = [MyPermission,]
    def get(self,request):
        return Response('美国电影列表')
    def post(self,request):
        pass

    def permission_denied(self, request, message=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated('无权访问')
        raise exceptions.PermissionDenied(detail=message)

class Jview(APIView):
    '''
    会员才可以看
    '''
    # authentication_classes = [MyAuthentication,]
    # permission_classes = [MyPermission,AdminPermission,]
    def get(self,request):
        return Response('日本电影列表')
    def post(self,request):
        pass

    def permission_denied(self, request, message=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated('无权访问')
        raise exceptions.PermissionDenied(detail=message)