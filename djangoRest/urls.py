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
]
