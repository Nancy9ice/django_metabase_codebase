"""
URL configuration for django_metabase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from affiliate_dashboard import views as affiliate_views
from affiliates import views as account_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("affiliates/", include('django.contrib.auth.urls')),
    path("login/", account_views.login_user, name="login"),
    path('affiliate_dashboard/<str:affiliate_name>/', affiliate_views.affiliate_dashboard, name='affiliate_dashboard'),
]
