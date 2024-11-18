"""victoravendaño URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from product import views as product_views

from django.conf import settings


urlpatterns = [
    path('', views.index, name="index.html"),
    path('Novedades/', views.about, name="Novdedades.html"),
    path('DLCs/', views.store, name="DLCs.html"),

    path('Juegos/', product_views.product, name="Juegos.html"),

    path('admin/', admin.site.urls),

    
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
