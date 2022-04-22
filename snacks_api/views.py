from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack
import json
from django.shortcuts import render

# Create your views here.
# controller function! (view in django - handles controls)
class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = SnackSerializer # tell django what serializer to use - turn into JSON objects 

# one request
class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all().order_by('id')
    serializer_class = SnackSerializer

#  define functions
def post(self, request, *args, **kwargs):
    file = request.data['file']
    image = Snack.objects.create(image=file)
    return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
