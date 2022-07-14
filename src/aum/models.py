import requests
from django.db import models, transaction

class Ban(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Charm(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    date_charm = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Distance(models.Model):
    
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=25)
    km = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

class Favorite(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Keyword(models.Model):
    
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=25)
    weight = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

class Visit(models.Model):
    
    id = models.AutoField(primary_key=True)
    aum_id = models.CharField(max_length=25)
    username = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    distance = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    measurement = models.CharField(max_length=255, null=True)
    nb_photo = models.IntegerField(null=True)
    desc = models.TextField(blank=True, null=True)
    shopping = models.TextField(blank=True, null=True)
    crack = models.TextField(blank=True, null=True)
    cant_stand = models.TextField(blank=True, null=True)
    popularity = models.IntegerField(null=True)
    hot = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    score = models.IntegerField(null=True)
    date_visit = models.DateTimeField(null=True)
    date_first_visit = models.DateTimeField(null=True)
    full_desc = models.TextField(blank=True,null=True)
    full_shopping = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


