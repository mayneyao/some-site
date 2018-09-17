"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, re_path


# from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register('post', api.PostViewSet)
# router.register('tag', api.TagViewSet)
# router.register('category', api.CategoryViewSet)

def blog(request):
    return HttpResponseRedirect('https://blog.gine.me')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('ocr/', include('ocr.urls')),
    path('gif/', include('altair.urls')),
    path('blog', blog),
    re_path(r'^$', blog),
]
