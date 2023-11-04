from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='images/') 
    image_name = models.CharField(max_length=255)
    isSelect = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.image_name
