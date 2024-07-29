from django.contrib import admin
from django.urls import path, include
from .views import home  # Importar la vista home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geography.urls')),  # Incluir las URLs del app geography
    path('', home, name='home'),  # Manejar la URL raíz con la vista home
]
