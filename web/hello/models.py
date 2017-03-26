from django.db import models
#from rest_framework import serializers

class Manufacturer(models.Model):
	mID = models.UUIDField(primary_key=True)
	timestamp = models.CharField(max_length=100)
	longitude = models.CharField(max_length=60)
	latitude = models.CharField(max_length=60)

class Drug(object):
	"""docstring for ClassName"""
	name =  models.CharField(max_length=60)
	expiration = models.CharField(max_length=100)
	strength =  models.DecimalField(decimal_places=2)

class Patient(object):
	"""docstring for Patient"""
	pID = None
	name =  models.CharField(max_length=60)
	timestamp = models.CharField(max_length=100)

class Pharmacy(object):
	"""docstring for Pharmacy"""
	phID = None
	name =  models.CharField(max_length=60)
	timestamp = models.CharField(max_length=100)
	latitude =  models.CharField(max_length=60)
	longitude =  models.CharField(max_length=60)
		
class Doctor(object):
	"""docstring for Doctor"""
	docID = None
	name = models.CharField(max_length=60)
	timestamp = models.CharField(max_length=100)
	refill = models.PositiveIntegerField()
	quantity = models.PositiveIntegerField()
	daily = models.PositiveIntegerField()
	
# class NFCdata(object):
# 	"""docstring for NFCdata"""
# 	manufacturer = None
# 	pharmacy = None
# 	patient = None
# 	doctor = None
		

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)



		
		


