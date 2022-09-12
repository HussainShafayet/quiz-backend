from turtle import title
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Question, Option , Answer
from .serializers import CategorySerializer, OptionSerializer, QuestionSerializer
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

@api_view(['GET','POST'])
def handleQuestion(request, quesId):
    if request.method == 'GET':
        ques = Question.objects.filter(category = quesId)
        quesSerializer = QuestionSerializer(ques, many = True).data
        data=[]
        for q in quesSerializer:
            opt = Option.objects.filter(question = q['id'])
            optSerializer = OptionSerializer(opt, many=True).data
            optdata = []
            for op in optSerializer:
                newOpt = {
                    'id': op['id'],
                    'title': op['title'],
                    'isCheckd': op['isCheckd']
                }
                optdata.append(newOpt)
            newQ = {
                'id': q['id'],
                'title': q['title'],
                'options': optdata
            }
            data.append(newQ)
        return Response({'success': True, 'data':data, 'status': status.HTTP_200_OK})
    elif request.method == 'POST':
        pass