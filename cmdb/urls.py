"""my_django_project URL Configuration

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
from cmdb import views
# from ipdb import set_trace
# set_trace()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^h.html', views.home),
    url(r'^login', views.login),
    url(r'^index1', views.index1),
    url(r'^user_info', views.user_info),
    url(r'^userdetail-(?P<nid>\d+)', views.userdetail),
    url(r'^orm', views.orm),
    # url(r'^home', views.Home.as_view()),
    url(r'^indexfffg/(?P<nid>\d+)/(?P<uid>\d+)/', views.index, name='indexx'),
    # url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail)  # def detail(request, *args, **kwargs)
]
