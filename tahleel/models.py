from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


# Create your models here.
# 
class Patient(models.Model):
	# user = models.OneToOneField(User,null=True,blank=True)
	name=models.CharField(max_length=1000,default='00000');
	national_id=models.IntegerField(unique=True,default='0');
	address=models.CharField(max_length=1000);
	password=models.CharField(max_length=1000,default='00000');
	def __str__(self):
		return self.name 



class LiverAnalysis(models.Model):
	Albumin=models.IntegerField(default='0')
	SGPT=models.IntegerField(default='0')
	SGOT=models.IntegerField(default='0')
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	

        
	 

class BloodAnalysis(models.Model):
	WBC=models.IntegerField(default='0')
	Platelets=models.IntegerField(default='0')
	RBC=models.IntegerField(default='0')
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	

		