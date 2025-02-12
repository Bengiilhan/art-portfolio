from django.db import models
from cloudinary.models import CloudinaryField

class Resim(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')  # Burada CloudinaryField kullanılıyor.

    def __str__(self):
        return self.title
# Create your models here.
