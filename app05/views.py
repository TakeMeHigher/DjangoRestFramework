from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.

#1基于url的get方式传参
class TestView(APIView):
    versioning_class = QueryParameterVersioning

    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request):
        self.dispatch
        #获取版本
        print(request.version)
        #获取版本管理的类
        print(request.versioning_scheme)


        #反向生成url
        reverse_url=request.versioning_scheme.reverse('test',request=request)
        print(reverse_url)

        return Response('get请求,当前版本为%s'%request.version)



    def post(self,request):
        pass

#2.基于url的正则方式传参
class TestView1(APIView):
    versioning_class =URLPathVersioning

    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        print(request.version)
        print(request.versioning_scheme)
        reverse_url=request.versioning_scheme.reverse('test',request=request)
        print(reverse_url)
        return Response('基于url的正则传参,版本为%s'%request.version)


