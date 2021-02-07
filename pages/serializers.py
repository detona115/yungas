from rest_framework import serializers
from .models import (
    Pessoa,
    Name,
    Location,
    Coordinate,
    Timezone,    
    Picture,
    Phone,
    Cell
)

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['large', 'medium', 'thumbnail']

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ['cell']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phone']

class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['offset', 'description']

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['latitude', 'longitude']

class LocationSerializer(serializers.ModelSerializer):
    timezones = TimezoneSerializer(many=True)
    coordinates = CoordinatesSerializer(many=True)
    class Meta:
        model = Location
        fields = ['street', 'city', 'state', 'postcode', 'coordinates', 'timezones']

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('title', 'first', 'last')

class PessoaSerializer(serializers.ModelSerializer):

    pictures = PictureSerializer(many=True, read_only=True)
    cells = CellSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)
    names = NameSerializer(many=True, read_only=True)
    class Meta:
        model = Pessoa
        fields = (
            'gender', 
            'names', 
            'locations', 
            'email', 
            'birthday', 
            'registered', 
            'phones', 
            'cells', 
            'pictures', 
            'nationality'
        )