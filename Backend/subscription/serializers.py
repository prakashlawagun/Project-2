from rest_framework import serializers
from .models import Packages


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'




