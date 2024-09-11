from django.db import models
from datetime import datetime

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Pool(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='pools')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name='teams')
    played=models.IntegerField( null=True)
    won=models.IntegerField( null=True)
    loss= models.IntegerField( null=True)
    draw=models.IntegerField( null=True)
    f=models.IntegerField( null=True)
    agg=models.IntegerField(null=True)
    plusminus=models.IntegerField( null=True)
    points= models.IntegerField( null=True)

    def __str__(self):
        return self.name
    

class Fixture(models.Model):

    STATUS = [
        ('upcoming', 'upcoming'),
        ('live', 'live'),
        ('played', 'played'),
        ('postponed', 'postponed'),
    ]

    home = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='home')
    away = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='away')
    status = models.CharField(max_length=100, null=True,choices=STATUS)
    homeresults = models.IntegerField(null=True)
    awayresults = models.IntegerField(null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.home) +" vs "  + str(self.away) 