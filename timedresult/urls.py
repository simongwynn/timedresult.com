"""timedresult URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from events import views
from events import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('RD/', views.road, name='Road'),
    path('TR/', views.track, name='Track'),
    path('CX/', views.cyclocross, name='Cyclo-Cross'),
    path('MTB/', views.mountainbike, name='Mountainbike'),
    path('GR/', views.gravel, name='Gravel'),
    path('<int:page_id>/', views.detail, name='detail'),
    path('<int:page_id>/startlist', views.startlist, name='startlist'),
    path('<int:page_id>/results', views.results, name='results'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
