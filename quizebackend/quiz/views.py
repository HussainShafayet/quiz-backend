from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

def hello(request):
    return Response('welcome')
