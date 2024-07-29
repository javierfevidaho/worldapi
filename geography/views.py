from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the CyberLotto Bank API!")

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
