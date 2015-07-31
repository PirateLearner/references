from django.shortcuts import render
from reference.models import Reference

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ReferenceList(APIView):
    def get(self, request, format=None):
        pass
    
    def post(self, request, format= None):
        pass
    
class ReferenceDetail(APIView):
    def get(self, request, pk, format=None):
        pass
    
    def put(self, request, pk, format=None):
        pass
    
    def delete(self, request, pk, format=None):
        pass