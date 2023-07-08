from datetime import timezone

from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
            blank=True, null=True)