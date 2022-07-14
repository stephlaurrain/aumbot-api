import requests
from django.db import models, transaction

class Distance(models.Model):
    
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=25)
    km = models.IntegerField(null=True)
    
    def __str__(self):
        return self.id

