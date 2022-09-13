from django.db import models
# from django.contrib.auth.models import User

class allData(models.Model):
    title = models.CharField(max_length = 200)
    price = models.CharField(max_length = 100)
    created_by = models.CharField(max_length = 180)
    description = models.CharField(max_length = 1000)
    def __str__(self):
        return self.title