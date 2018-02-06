from django.shortcuts import render

from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.exceptions import APIException


from app01 import models
# Create your views here.

class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token=request.query_params.get('token')
        user=models.Userinfo.objects.filter(token=token).first()
        if user:
            return (user.name,user)
        return None

class MyPermission(object):
    message = '登录才可以访问'
    def has_permission(self,request, view):
        if request.user:
            return True
        return False

class AdminPermission(object):
    message = '会员才可以访问'
    def has_permission(self,request,view):
        if request.user=='ctz':
            return True
        return False