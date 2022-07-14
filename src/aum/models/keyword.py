import requests
from django.db import models, transaction

class Keyword(models.Model):
    
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=25)
    weight = models.IntegerField(null=True)
    
    def __str__(self):
        return self.word