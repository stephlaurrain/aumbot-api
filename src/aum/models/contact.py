import requests
from django.db import models, transaction

class Contact(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    
    def __str__(self):
        return self.aum_id
