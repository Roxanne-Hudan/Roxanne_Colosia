"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path, include
# from config.urls import probandoTemplate
from core import views as core_views # Esta parte lo hice antes por la app que se tenia originalmente y no chcoaran las views
from AppCoder import views as AppCoder_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("AppCoder/", include("AppCoder.urls")), # la Urls de la clase del 03/06
    path("index/", core_views.index),
    path("index2/", core_views.index2),
    path("Saludar/", core_views.saludar),
    path("saludar2/", core_views.saludar_con_etiqueta),
    path('saludar3/<str:nombre>/<str:apellido>', core_views.saludar_con_parametros),
    path("blog/", core_views.blog),
    path("App/", AppCoder_views.App)
    


]
