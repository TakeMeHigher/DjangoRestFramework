from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.response import Response
# Create your views here.

#1基于正则的方式传参
class TestView(APIView):
    versioning_class = QueryParameterVersioning

    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request):
        #获取版本
        print(request.version)
        #获取版本管理的类
        print(request.versioning_scheme)

        return Response('get请求,当前版本为%s'%request.version)



    def post(self,request):
        pass

