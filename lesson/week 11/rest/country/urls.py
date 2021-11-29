from django.urls import path
from country.views import CountryListAPIView

urlpatterns = [
    # path('country/', AllCountryAPIView.as_view()),
    path('country-new/', CountryListAPIView.as_view()),
]