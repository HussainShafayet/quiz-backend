from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST '])
def hello(request):
    if request.method == 'GET':
        return Response({'success'})
    elif request.method == 'POST':
        return Response({'sucess'})
