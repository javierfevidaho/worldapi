from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geography.urls')),  # Include geography app URLs
    path('', home, name='home'),  # Add this line to handle the root URL
]
