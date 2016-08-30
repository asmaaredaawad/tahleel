from django.conf.urls import url
from django.contrib import admin
from tahleel.views import *

urlpatterns = [
    url(r'^$',home),
    url(r'^login_employee/$',login_employee),
    url(r'^check/$',sigin),
    url(r'^login_patient/$',login_patient),
    url(r'^check_pat/$',sigin_pat),
    url(r'^invalid_pat/$',invalid_pat),

   	url(r'^login/$',login),
   	# url(r'^auth/$',sigin),
    # url(r'^loggedin/$',loggedin),
    url(r'^invalid/$',invalid),
        url(r'^logout/$',logout),

    # add new patient
    url(r'^add_patient/$',add_patient),
    url(r'^add/$',add),
    url(r'^display/$',dispaly_all_patient),

    # check web services
    url(r'^display_web_service/$',dispaly),
    url(r'^login_web_service/$',login_web_service),

    url(r'^(?P<patient_id>[0-9]+)/edit_patient$',edit_patient),
    url(r'^(?P<patient_id>[0-9]+)/edit_p/$',edit),

    url(r'^(?P<patient_id>[0-9]+)/delete_patient$',delete_patient),
    url(r'^(?P<patient_id>[0-9]+)/more_patient$',more_patient),
    # Analysis
    url(r'^(?P<patient_id>[0-9]+)/liver$',liver),
    url(r'^(?P<patient_id>[0-9]+)/add_liver/$',add_liver),
    url(r'^(?P<patient_id>[0-9]+)/(?P<liver_id>[0-9]+)/edit_liver$',edit_liver),
    url(r'^(?P<patient_id>[0-9]+)/(?P<liver_id>[0-9]+)/edit_l/$',edit_l),
    url(r'^(?P<patient_id>[0-9]+)/(?P<liver_id>[0-9]+)/delete_liver/$',delete_liver),

    url(r'^(?P<patient_id>[0-9]+)/blood$',blood),
    url(r'^(?P<patient_id>[0-9]+)/add_blood/$',add_blood),
    url(r'^(?P<patient_id>[0-9]+)/(?P<blood_id>[0-9]+)/edit_blood$',edit_blood),
    url(r'^(?P<patient_id>[0-9]+)/(?P<blood_id>[0-9]+)/edit_b/$',edit_b),
    url(r'^(?P<patient_id>[0-9]+)/(?P<blood_id>[0-9]+)/delete_blood/$',delete_blood),
     
    # url(r'^(?P<liver_id>[0-9]+)/edit_l/$',edit_l),

    # url(r'^(?P<patient_id>[0-9]+)/blood$',blood),








    ]
