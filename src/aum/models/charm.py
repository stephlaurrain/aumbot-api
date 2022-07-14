import requests
from django.db import models, transaction

class Charm(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    date_charm = models.DateTimeField(null=True)

    def __str__(self):
        return self.aum_id