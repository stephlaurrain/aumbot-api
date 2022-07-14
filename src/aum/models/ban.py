import requests
from django.db import models, transaction

class Ban(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.aum_id