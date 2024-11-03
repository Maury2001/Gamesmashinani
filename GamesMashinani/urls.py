"""
URL configuration for GamesMashinani project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from Games import views as game_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', game_view.Home, name='home'),
    path('', game_view.Dash, name='dashboard'),
    path('regionform/', game_view.RegionAdj, name='regionform'),
    path('teamform/', game_view.TeamAdj, name='teamform'),
    path('poolform/', game_view.PoolAdj, name='poolform'),
    path('kiambutable/', game_view.KiambuTable, name='kiambutable'),
    path('murangatable/', game_view.MurangaTable, name='murangatable'),
    path('pooltable/<str:pk>/', game_view.Table, name='pooltable'),
    path('fixtures/', game_view.Fix, name='fixtures')
]