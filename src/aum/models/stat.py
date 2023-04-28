import requests
from django.db import models, transaction

class Stat(models.Model):
    
    id = models.AutoField(primary_key=True)
    date_stat = models.DateTimeField(blank=True, null=True)
    age_min = models.IntegerField(null=True)
    age_max = models.IntegerField(null=True)
    nb_online = models.IntegerField(null=True)
        
    def __str__(self):
        return f"{self.date_stat} - {self.age_min} - {self.age_max} - {self.nb_online}"