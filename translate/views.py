from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.parsers import JSONParser 

from .forms import InputForm
from .models import Input 
from .serializers import InputSerializer 

import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 


class CodeTranslation(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer

def home(request):

    if request.method=='POST':  
        # Create a form instance and populate with data given by user
        form = InputForm(request.POST or None)

        # Checking validity: 
        if form.is_valid(): 
            
            # Extract user inputs
            source_language = form.cleaned_data['source_language']
            source_code = form.cleaned_data['source_code']
            target_language = form.cleaned_data['target_language']

            return HttpResponseRedirect('result')


        # DO STUFF WITH DATA
        # 1. Test with small model
        # 2. Make it pretty
        # 3. Ajax (reroute to same page)
        # 4. Connect actual model
        # 5. Create rest API

    # Creates empty form on GET request
    else: 
        form = InputForm()

    return render(request, 'home.html', {'form': form})

def result(request):
    return render(request, 'result.html')
