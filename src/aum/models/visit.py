import requests
from django.db import models, transaction

class Visit(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(blank=True, max_length=25)
    username = models.CharField(blank=True, max_length=255, null=True)
    city = models.CharField(blank=True, max_length=255, null=True)
    distance = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, max_length=255, null=True)
    measurement = models.CharField(blank=True, max_length=255, null=True)
    nb_photo = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    shopping = models.TextField(blank=True, null=True)
    crack = models.TextField(blank=True, null=True)
    cant_stand = models.TextField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    hot = models.DecimalField(blank=True, max_digits=3, decimal_places=2, null=True)
    score = models.IntegerField(blank=True, null=True)
    date_visit = models.DateTimeField(blank=True, null=True)
    date_first_visit = models.DateTimeField(blank=True, null=True)
    full_desc = models.TextField(blank=True,null=True)
    full_shopping = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.aum_id


