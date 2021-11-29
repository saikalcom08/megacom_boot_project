from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from .models import Country
from .serializers import CountryListSerializers


# Create your views here.
# class AllCountryAPIView(APIView):
#     def get(self, request):
#         queryset = Country.objects.all()
#         serializer = CountryListSerializers(instance=queryset, many=True)
#         return Response(serializer.data)

class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializers
