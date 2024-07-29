from django.urls import path
from .views import CountryList, CountryDetail, CityList, CityDetail

urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
    path('cities/', CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city-detail'),
]
