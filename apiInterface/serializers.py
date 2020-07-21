from rest_framework import serializers
from owner.models import Cars
from .models import dashboardData

class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cars
        fields ='__all__'

class DashboardSerializers(serializers.ModelSerializer):
    class Meta:
        model= dashboardData
        fields ='__all__'