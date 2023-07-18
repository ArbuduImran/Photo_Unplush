from django.db import models

class Photo(models.Model):
    keyword = models.CharField(max_length=100)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)