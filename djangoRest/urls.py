"""djangoRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from app02 import views as app02_views
from app03 import views as app03_views
from app04 import views as app04_views
from app05 import views as app05_views
from app06 import views as app06_views
from app07 import views as app07_views
from app08 import views as app08_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hosts/', views.HostView.as_view()),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^users/', views.Userview.as_view()),
    url(r'^sals/', views.Salview.as_view()),


    url(r'^p/', app02_views.Pview.as_view()),
    url(r'^mp/', app02_views.Aview.as_view()),
    url(r'^jp/', app02_views.Jview.as_view()),



    url(r'^limit/', app03_views.Limitview.as_view()),



    url(r'^index/', app04_views.IndexView.as_view()),
    url(r'^user/', app04_views.UserView.as_view()),
    url(r'^manage/', app04_views.ManageView.as_view()),



    url(r'^test/', app05_views.TestView.as_view(),name='test'),
    url(r'^(?P<version>[v1|v2]+)/test1/', app05_views.TestView1.as_view(),name='test'),

    url(r'^ser/', app06_views.SerView.as_view()),

    url(r'^page/', app07_views.UserListView.as_view()),



    url(r'^userlist/$', app08_views.UserListView.as_view({'get':'list','post':'create'})),
    url(r'^userlist/(?P<pk>\d+)$', app08_views.UserListView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
]
