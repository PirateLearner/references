'''
Created on 24-Jul-2015

@author: anshul
'''
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')