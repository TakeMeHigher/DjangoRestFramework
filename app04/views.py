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