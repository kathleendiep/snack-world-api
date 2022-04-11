from rest_framework import serializers 
from .models import Snack

class SnackSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Snack # tell django which model to use
        fields = ('id', 'name', 'category', 'city', 'country', 'description') # tell django which fields to include