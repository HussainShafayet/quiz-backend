from turtle import title
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Question, Option , Answer
from .serializers import CategorySerializer
from rest_framework import status

# Create your views here.

@api_view(['GET','POST '])
def handleCategory(request):
    if request.method == 'GET':
        catg = Category.objects.all()
        catgSerializer = CategorySerializer(catg, many=True).data
        data = []
        for obj in catgSerializer:
            newObj = {
                'id': obj['id'],
                'title': obj['title'],
            }
            data.append(newObj)
        return Response({'success': True, 'data':data, 'status': status.HTTP_200_OK})
    elif request.method == 'POST':
        return Response({'sucess'})
