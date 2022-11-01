from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')

