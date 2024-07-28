from django.urls import path
from .views import CountryList, CountryDetail

urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
]
