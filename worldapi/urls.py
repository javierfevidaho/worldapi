# worldapi/urls.py

from django.contrib import admin
from django.urls import path, include
from geography.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geography.urls')),
    path('', home, name='home'),
]
