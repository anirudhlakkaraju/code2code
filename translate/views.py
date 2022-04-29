from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InputForm
# Create your views here.


def home(request):

    if request.method=='POST':  
        # Create a form instance and populate with data given by user
        form = InputForm(request.POST)

        # Checking validity: 
        if form.is_valid(): 
            return HttpResponseRedirect('result')

    else: 
        form = InputForm()

    return render(request, 'home.html', {'form': form})

def result(request):
    return render(request, 'result.html')
