from django.db import models
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    # need to set default as ''
    image = models.FileField(upload_to='uploaded_image', default='')






    
