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
from .model import inference_utils, process_outputs
from translate.model.predict import predict 

import torch
import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 



# def process_python_output(prediction):
#     lines = prediction.split("NEW_LINE")
#     curr_indent = 0
#     new_lines = []
#     for line in lines:
#         indent_count = line.count('INDENT')
#         dedent_count = line.count('DEDENT')
#         curr_indent += indent_count - dedent_count
#         new_lines.append('\t'*curr_indent + line.replace('INDENT', '').replace('DEDENT', ''))
#     return "\n".join(new_lines)


# def predict(source_language, target_language, source_code):

#     device = torch.device("cuda")
#     model_type = "plbart"
#     model, tokenizer = get_model(model_type, source_language, target_language)
#     model.to(device)

#     eval_batch_size = 1
#     max_source_length, max_target_length = 400, 400

#     eval_examples, eval_dataloader = get_eval_dataloader(source_code, eval_batch_size, 
#                                                         max_source_length, max_target_length, tokenizer)

#     pred = sample_generation_single(eval_examples, eval_dataloader, model, model_type, tokenizer, 
#                             max_target_length, device)

#     return process_python_output(pred[0])


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
        translated_code = predict(source_language, target_language, source_code)

        # Make translated code pretty
        translated_code = process_outputs.pretty(translated_code, target_language)

        # Return translated code to AJAX call       
        return JsonResponse({"Response":translated_code})

    else:
        # Empty Endpoint
        return HttpResponse("Works!")
