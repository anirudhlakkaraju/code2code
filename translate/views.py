from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

from .forms import InputForm
from .models import Input 
from .model import inference_utils, process_outputs
from translate.model.predict import predict 

import torch
import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
import time
from django.shortcuts import render, redirect 
from django.contrib import messages 

def index(request):
# Reroutes localhost/ to localhost/home
    return HttpResponseRedirect('/home')


def home(request):
    # Creates empty form on GET request
    form = InputForm()
    return render(request, 'home.html', {'form': form})


def translate(request):
    
    # Receive the inputs as a POST request from AJAX call
    if request.method=='POST':

        # Load user inputs
        response = json.loads(request.body)

        # Extract user inputs
        source_language = response['sourceLanguage']
        source_code = response['sourceCode']
        target_language = response['targetLanguage']

        # Return source code if user selects same source and target languages
        if source_language==target_language:
            return JsonResponse({"Response":source_code})

        # Predict target code
        # translated_code = predict(source_language, target_language, source_code)

        # Make translated code pretty
        # translated_code = process_outputs.pretty(translated_code, target_language)

        time.sleep(3)

        # Return translated code to AJAX call       
        return JsonResponse({"Response":source_code})

    else:
        # Empty Endpoint
        return HttpResponse("GET endpoint!")
