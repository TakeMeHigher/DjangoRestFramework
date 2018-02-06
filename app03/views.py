import time

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import BaseThrottle
from rest_framework.throttling import SimpleRateThrottle
from rest_framework import exceptions
# Create your views here.


AllOW={}

class MyThrottle(BaseThrottle):
    '''
    要求每分钟只能访问十次
    '''
    ip = '1.1.1.1'
    def allow_request(self, request, view):

        ctime=time.time()
        ip=self.ip
        if ip not in AllOW:
            AllOW[ip]=[ctime,]
        else:
            time_list=AllOW[ip]
            while True:
                if ctime-60>time_list[-1]:
                    time_list.pop()
                else :
                    break
            if len(AllOW[ip])>10:
                return False
            AllOW[ip].insert(0,ctime)
        return True

    def wait(self):
        ip=self.ip
        ctime=time.time()
        first_in_time=AllOW[ip][-1]
        wt=60-(ctime-first_in_time)
        return wt


class MySimpleRateThrottle(SimpleRateThrottle):
    #必须要写因为SimpleRateThrottle中要求了必须写
    '''
     def get_rate(self):
        """
        Determine the string representation of the allowed request rate.
        """
        #判断当前类中我们定义的scope是否有值，没有则抛出异常，告诉我们必须设置scope
        if not getattr(self, 'scope', None):
            msg = ("You must set either `.scope` or `.rate` for '%s' throttle" %
                   self.__class__.__name__)
            raise ImproperlyConfigured(msg)
    '''
    scope = 'tiga'

    #也必须必须要写
    '''
        def get_cache_key(self, request, view):
        """
        Should return a unique cache-key which can be used for throttling.
        Must be overridden.

        May return `None` if the request should not be throttled.
        """
        raise NotImplementedError('.get_cache_key() must be overridden')
    '''
    def get_cache_key(self, request, view):
        return self.get_ident(request)



class Limitview(APIView):
    throttle_classes=[MySimpleRateThrottle,]
    def get(self,reques):
        return Response('欢迎访问')

    def throttled(self,request,wait):
        class InnerThrottled(exceptions.Throttled):
            default_detail = '请求被限制.'
            extra_detail_singular = 'Expected available in {wait} second.'
            extra_detail_plural = '还需要再等待{wait}秒'

        raise InnerThrottled(wait)
