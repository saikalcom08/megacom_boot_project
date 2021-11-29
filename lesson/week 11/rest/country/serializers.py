from rest_framework import serializers


class CountryListSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    capital = serializers.CharField(max_length=100)
    population = serializers.IntegerField()
    # president = serializers.IntegerField(source='president.id')
    president = serializers.CharField(max_length=100, source='president.username')