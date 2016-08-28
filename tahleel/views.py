from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.context_processors import csrf

from django.contrib.auth import authenticate
from .forms import *
from backends import *
import json


from .models import *

# Create your views here.
def home(request):
	return render_to_response('tahleel/home.html')

# login as employee
def login_employee(request):
	c= {}
	c.update(csrf(request))
	return render_to_response('tahleel/login_Emp.html',c)

def sigin(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	user=authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		# print "asmaa"
		return render_to_response('tahleel/Emp_home.html')
	else:
		# print "not asmaa"
		# return render_to_response('tahleel/invalid.html')
		return HttpResponseRedirect('/tahleel/invalid')


def invalid(request):
	c= {}
	c.update(csrf(request))
	return render(request, 'tahleel/invalid.html',c)			

# login as patient
def login_patient(request):
	c= {}
	c.update(csrf(request))
	return render_to_response('tahleel/login_pat.html',c)

def sigin_pat(request):
	national_id=request.POST.get('national_id')
	password=request.POST.get('password')

	patient1=Patient.objects.filter(national_id=national_id,password=password).exists()
	if patient1 :
		patient=Patient.objects.filter(national_id=national_id,password=password).values()
		patient2=Patient.objects.get(national_id=national_id)
		liver=patient2.liveranalysis_set.all()
		blood=patient2.bloodanalysis_set.all()
		context={'patient':patient,'liver':liver,'blood':blood}
		print('found')
		return render(request,'tahleel/pat_home.html',context)
	else:
		print(' not found')
		# return render_to_response('tahleel/login_pat.html',c)
		return HttpResponseRedirect('/tahleel/login_patient')	
		# return render_to_response('tahleel/invalid_pat.html')

# for recive request from web services
def login_web_service(request):
	national_id=request.POST.get('name')
	password=request.POST.get('password')
	c= {}
	c.update(csrf(request))
	data={}
	data['national_id']=national_id
	data['password']=password
	data['c']=c
	json_data=json.dumps(str(data))
	return HttpResponse(json_data,content_type='application/json')
	# patient1=Patient.objects.filter(national_id=national_id,password=password).exists()
	# if patient1 :
	# 	patient=Patient.objects.filter(national_id=national_id,password=password).values_list()
	# 	json_data = json.dumps(str(patient))
	# 	return HttpResponse(json_data, content_type='application/json')
	# else:
	# 	return HttpResponse('failed',content_type='application/json')	

# for web services 
def dispaly(request):
	patients=Patient.objects.all().values_list();
	# context = {'patients':patients}
	json_data = json.dumps(str(patients))
	return HttpResponse(json_data, content_type='application/json')
	# print(json_data) 


def invalid_pat(request):
	c= {}
	c.update(csrf(request))
	return render(request, 'tahleel/invalid_pat.html',c)			
# _______________________________________________________________________


 #add new patient
def add_patient(request):
	c= {}
	c.update(csrf(request))
 	return render_to_response('tahleel/add_patient.html',c)

def add(request):	
	if request.method == 'POST':
		form = PatientForm(request.POST,request.FILES)
		name=request.POST.get('name')
		national_id=request.POST.get('national_id')
		address=request.POST.get('address')
		password =request.POST.get('password')
		new_patient= Patient(name=name,national_id=national_id,address=address,password=password)
		new_patient.save()
		return HttpResponseRedirect('/tahleel/display')
	else:
		form = PatientForm()
	return render(request,'tahleel/add_patient.html',{'form': form})

#display_all_patient
def dispaly_all_patient(request):
	patients=Patient.objects.all();
	context = {'patients':patients}
	return render(request,'tahleel/patients.html',context)

# edit patient
def edit_patient(request,patient_id):
	patient = Patient.objects.get(pk=patient_id)
	context = {'patient':patient}
	return render(request,'tahleel/edit_patient.html',context)

def edit(request,patient_id):
	name = request.POST['name']
	national_id = request.POST['national_id']
	address = request.POST['address']
	# password = request.POST['password']
	patient=Patient.objects.filter(pk=patient_id).update(
		name=name,
		national_id=national_id,
		address=address
		# password=password,
		)
	# context = {'patient':patient}
	return HttpResponseRedirect('/tahleel/display')

def delete_patient(request,patient_id):
	Patient.objects.get(id = patient_id).delete()
	return HttpResponseRedirect('/tahleel/display')

def more_patient(request,patient_id):
	patient = Patient.objects.get(pk=patient_id)
	liver = patient.liveranalysis_set.all()
	blood = patient.bloodanalysis_set.all()

	context = {'patient':patient,'liver':liver,'blood':blood}
	return render(request,'tahleel/display_patient.html',context)
# __________________________________________________________________

#liver
def liver(request,patient_id):
 	patient = Patient.objects.get(pk=patient_id)
 	c= {}
	c.update(csrf(request))
	context = {'patient':patient,'c':c}
	return render(request,'tahleel/add_liver.html',context)

def add_liver(request,patient_id):
	if request.method == 'POST':
		form = LiverForm(request.POST,request.FILES)
		Albumin=request.POST.get('Albumin')
		SGPT=request.POST.get('SGPT')
		SGOT=request.POST.get('SGOT')
		# patient_id =request.POST.get('patient_id')
		patient = Patient.objects.get(pk=patient_id)
		new_liver_analysis= LiverAnalysis(Albumin=Albumin,SGPT=SGPT,SGOT=SGOT,patient=patient)
		new_liver_analysis.save()
		return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id)
		
	else:
		form = LiverForm()
	return render(request,'tahleel/add_liver.html',{'form': form})	

def edit_liver(request,patient_id,liver_id):
	patient = Patient.objects.get(pk=patient_id)
	liver = patient.liveranalysis_set.filter(pk=liver_id).values()
	# print(liver)
	# liver = liver.objects.get(pk=liver_id)
	context = {'patient':patient,'liver':liver}
	return render(request,'tahleel/edit_liver.html',context)

def edit_l(request,patient_id,liver_id):
	Albumin = request.POST['Albumin']
	SGPT = request.POST['SGPT']
	SGOT = request.POST['SGOT']
	patient = Patient.objects.get(pk=patient_id)
	# liver = patient.liveranalysis_set.filter(pk=liver_id).values()
	# print(liver)
	liver = patient.liveranalysis_set.filter(pk=liver_id).update(
		Albumin=Albumin,
		SGPT=SGPT,
		SGOT=SGOT
		)	
	return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id)

def delete_liver(request,patient_id,liver_id):
	patient = Patient.objects.get(pk=patient_id)
	liver = patient.liveranalysis_set.filter(pk=liver_id).delete()
	return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id)

#_____________________________________________________________________
 #Blood 
def blood(request,patient_id):
 	patient = Patient.objects.get(pk=patient_id)
 	c= {}
	c.update(csrf(request))
	context = {'patient':patient,'c':c}
	return render(request,'tahleel/add_blood.html',context)

def add_blood(request,patient_id):
	if request.method == 'POST':
		form = BloodForm(request.POST,request.FILES)
		Platelets=request.POST.get('Platelets')
		RBC=request.POST.get('RBC')
		WBC=request.POST.get('WBC')
		# patient_id =request.POST.get('patient_id')
		patient = Patient.objects.get(pk=patient_id)
		new_blood_analysis= BloodAnalysis(Platelets=Platelets,RBC=RBC,WBC=WBC,patient=patient)
		new_blood_analysis.save()
		return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id)
		
	else:
		form = BloodForm()
	return render(request,'tahleel/add_Blood.html',{'form': form})	

def edit_blood(request,patient_id,blood_id):
	patient = Patient.objects.get(pk=patient_id)
	blood = patient.bloodanalysis_set.filter(pk=blood_id).values()
	# print(blood)
	# blood = blood.objects.get(pk=blood_id)
	context = {'patient':patient,'blood':blood}
	return render(request,'tahleel/edit_blood.html',context)

def edit_b(request,patient_id,blood_id):
	Platelets = request.POST['Platelets']
	RBC = request.POST['RBC']
	WBC = request.POST['WBC']
	patient = Patient.objects.get(pk=patient_id)
	# blood = patient.bloodanalysis_set.filter(pk=blood_id).values()
	# print(blood)
	blood = patient.bloodanalysis_set.filter(pk=blood_id).update(
		Platelets=Platelets,
		RBC=RBC,
		WBC=WBC
		)	
	return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id)

def delete_blood(request,patient_id,blood_id):
	patient = Patient.objects.get(pk=patient_id)
	blood = patient.bloodanalysis_set.filter(pk=blood_id).delete()
	return HttpResponseRedirect('/tahleel/%s/more_patient'% patient_id) 		 	


