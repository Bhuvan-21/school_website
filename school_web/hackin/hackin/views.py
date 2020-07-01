from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from sdatabase.forms import UserCreationForm
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('ml')
    else:
        form = UserCreationForm()
    return render(request,"index.html",{'form':form})

import tensorflow as tf
import numpy as np
from tensorflow import keras
from ml.models import mod
import re,string
from ml.forms import mlform
# Create your views here.
dicti={
    'F':1,
    'M':0,
    'U':0,
    'R':1,
    'LE3':0,
    'GT3':1,
    'T':0,
    'A':1,
    'at_home':0,
    'health':1,
    'services':2,
    'teacher':3,
    'other':4,
    'home':0,
    'reputation':1,
    'course':2,
    'other reason':3,
    'legal-guardian':2,
    'mother':0,
    'father':1,
    'no':0,
    'yes':1,
}

def mlview(request):
    X=np.zeros((1,31),dtype=np.int32)
    model=tf.keras.models.load_model(r'C:\Users\ARYAN JAIN\hack2')
    if request.method=='POST':
        mform=mlform(request.POST)
        if mform.is_valid():
            mform.save()
            modl=get_list_or_404(mod)
            mod1=modl[-1]
            X[0][0]=dicti[mod1.get_gender()]
            X[0][1]=mod1.get_age()
            X[0][2]=dicti[mod1.get_famsize()]
            X[0][3]=dicti[mod1.get_pstatus()]
            X[0][4]=dicti[mod1.get_address()]
            X[0][5]=mod1.get_medu()
            X[0][6]=mod1.get_fedu()
            X[0][7]=dicti[mod1.get_mjob()]
            X[0][8]=dicti[mod1.get_fjob()]
            X[0][9]=dicti[mod1.get_reason()]
            X[0][10]=dicti[mod1.get_guardian()]
            X[0][11]=mod1.get_traveltime()
            X[0][12]=mod1.get_stime()
            X[0][13]=mod1.get_failure()
            X[0][14]=dicti[mod1.get_schoolsup()]
            X[0][15]=dicti[mod1.get_famsup()]
            X[0][16]=dicti[mod1.get_paid()]
            X[0][17]=dicti[mod1.get_activities()]
            X[0][18]=dicti[mod1.get_nursery()]
            X[0][19]=dicti[mod1.get_higher()]
            X[0][20]=dicti[mod1.get_internet()]
            X[0][21]=mod1.get_famrel()
            X[0][22]=0
            X[0][23]=mod1.get_freetime()
            X[0][24]=mod1.get_goout()
            X[0][25]=mod1.get_dalc()
            X[0][26]=mod1.get_walc()
            X[0][27]=mod1.get_health()
            X[0][28]=mod1.get_absences()
            X[0][29]=mod1.get_g1()
            X[0][30]=mod1.get_g2()
    else:
        mform=mlform()
    pr=0
    pr=model.predict(X)[0][0]
    absences=X[0][28]
    dalc=X[0][25]
    goout=X[0][24]
    freetime=X[0][23]
    g1=X[0][29]
    g2=X[0][30]
    traveltime=X[0][11]
    stime=X[0][12]
    return render(request,'ml1.html',{'mform':mform,'traveltime':traveltime,'stime':stime,'pr':pr,'absences':absences,'freetime':freetime,'goout':goout,'dalc':dalc,'g1':g1,'g2':g2})
