
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class PatientForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    national_id= forms.CharField(label='national_id', max_length=100)
    address = forms.CharField(label='address',widget=forms.Textarea)
    password = forms.CharField(label='password')        


class LiverForm(forms.Form):
    Albumin = forms.IntegerField(label='Liver lbumin')
    SGPT= forms.IntegerField(label='Liver SGPT')
    SGOT = forms.IntegerField(label='Liver SGOT')
  

class BloodForm(forms.Form):
    Platelets = forms.IntegerField(label=' Blood Platelets')
    RBC= forms.IntegerField(label='Blood RBC')
    WBC = forms.IntegerField(label='Blood WBC')

