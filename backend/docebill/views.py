from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilaizer import *
from .models import * 
 

@api_view(['GET','POST'])
def home(request):
    dc =Doctor.objects.all()
    ctor= {'name':'doctor','xxx':'yyyy','fff':'yyyy'}
    return Response(dc)
# def baes([])