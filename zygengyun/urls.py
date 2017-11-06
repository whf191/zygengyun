"""zygengyun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from gengyun.views import  gengyun_index,gengyun_zhongzi,zhongzi_open
from gengyun.houtai_views import  gengyun_login,gengyun_denglu,gengyun_logout,houtai_admin,\
    houtai_admin_grxx,houtai_admin_gyzz,houtai_admin_wdgy,houtai_fayan,zhongzi_fayan

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gengyun_index/',gengyun_index),
    url(r'^gengyun_zhongzi/',gengyun_zhongzi),
    url(r'^zhongzi_open/',zhongzi_open),
url(r'^gengyun_login/',gengyun_login),
url(r'^gengyun_denglu/',gengyun_denglu),
url(r'^gengyun_logout/',gengyun_logout),

url(r'^houtai_admin/',houtai_admin),
url(r'^houtai_admin_grxx/',houtai_admin_grxx),
url(r'^houtai_admin_gyzz/',houtai_admin_gyzz),
url(r'^houtai_admin_wdgy/',houtai_admin_wdgy),
url(r'^houtai_fayan/',houtai_fayan),
url(r'^zhongzi_fayan/',zhongzi_fayan),





]
