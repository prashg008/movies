"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.urls import user_router
from utils.views import request_count, reset_request_count
from collection.urls import collection_router
from collection.views import movies_list


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(user_router.urls)),
    url(r'', include(collection_router.urls)),
    url(r'request-count/reset/', reset_request_count),
    url(r'request-count/', request_count),
    url(r'movies/', movies_list)
]
