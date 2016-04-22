from __future__ import unicode_literals

from django.db import models

# Create your models here.
class professor(models.Model):
	fullname = models.CharField(max_length=120)
	email = models.EmailField()
	phone = models.IntegerField()



class reviews(models.Model):
	course =  models.CharField(max_length=120)
	profname =  models.CharField(max_length=120)
	reviews =  models.CharField(max_length=350)


def __unicode__(self):
		return self.professor