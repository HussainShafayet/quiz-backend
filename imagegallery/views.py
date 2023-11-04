from turtle import title
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Image
from .serializers import ImageSerializer
from rest_framework import status
import json

# Create your views here.

@api_view(['GET','POST'])
def handleImage(request):
    if request.method == 'GET':
        imgs = Image.objects.all()
        imgSerializer = ImageSerializer(imgs, many = True).data
        data=[]
        for q in imgSerializer:
            data.append(q)
        return Response({'success': True, 'data':data, 'status': status.HTTP_200_OK})
    elif request.method == 'POST' and request.FILES.get('file'):
        image_name = request.FILES['file'].name
        is_select = request.POST.get('is_select', False)
        is_featured = request.POST.get('is_featured', False)

        image = Image(file=request.FILES['file'], image_name=image_name, isSelect=is_select, isFeatured=is_featured)
        image.save()
        
        image_serializer = ImageSerializer(image)
        return Response({'success': True, 'data':image_serializer.data, 'status': status.HTTP_200_OK})

@api_view(['DELETE'])
def handleImageDelete(request):
     if request.method == 'DELETE':
        try:
            data = json.loads(request.body)  # Parse the JSON array from the request body
            for id in data:
                imgObj = Image.objects.get(id=id)
                imgObj.delete()
            return  Response({'success': True, 'message':'Image Delete Successful', 'status': status.HTTP_200_OK})
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data in the request body'}, status=400);
        except Exception as e:
            return  Response({'success': False, 'message':{e}, 'status': 500})