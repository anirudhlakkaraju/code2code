from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
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


# class CodeTranslation(viewsets.ModelViewSet):
#     queryset = Input.objects.all()
#     serializer_class = InputSerializer

# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):

    # if request.method=='POST' :  
    #     # Create a form instance and populate with data given by user
    #     form = InputForm(request.POST)
    #     # Checking validity: 
    #     if form.is_valid(): 
            
    #         # Extract user inputs
    #         source_language = form.cleaned_data['source_language']
    #         source_code = form.cleaned_data['source_code']
    #         target_language = form.cleaned_data['target_language']

    #         # PREDICT TARGET CODE

    #         translated_code = source_code
    #         return json.dumps({"submitted":"True"})

    
    
    # Creates empty form on GET request
    form = InputForm()
    return render(request, 'home.html', {'form': form})


def translate(request):
    
    # Receive the inputs as a POST request from AJAX call
    if request.method=='POST':

        # Load user inputs
        response = json.loads(request.body)

        # print(response)

        # Extract user inputs
        source_language = response['sourceLanguage']
        source_code = response['sourceCode']
        target_language = response['targetLanguage']

        # PREDICT TARGET CODE
        # ....

        translated_code = source_code
    
        # Return translated code to AJAX call       
        return JsonResponse({"Response":translated_code})

    else:
        # Empty Endpoint
        return HttpResponse("Works!")
