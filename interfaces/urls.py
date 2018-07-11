"""interfaces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from interfaz.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('registro', RegistroView.as_view(), name='registro'),
    path('home', HomeView.as_view(), name='home'),
    path('menu', MenuView.as_view(), name='menu'),
    path('faq', FaqView.as_view(), name='faq'),
    path('report', ReportView.as_view(), name='report'),
    path('search', SearchView.as_view(), name='search'),
    path('logout', salir, name='logout'),
    #path('<string:path>', 'django.views.static.serve',{'document_root', settings.STATIC_ROOT})
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
