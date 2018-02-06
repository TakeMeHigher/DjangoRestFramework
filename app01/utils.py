from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework import serializers

from app01 import models



class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        user=models.Userinfo.objects.filter(token=token).first()
        if user:
            return (user.name, 'aaaaaa')
        raise APIException('认证失败')