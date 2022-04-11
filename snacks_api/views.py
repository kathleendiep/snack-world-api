from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack

# Create your views here.
# controller function! (view in django - handles controls)
class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = SnackSerializer # tell django what serializer to use - turn into JSON objects 

# one request
class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all().order_by('id')
    serializer_class = SnackSerializer