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
        imgs = Image.objects.all().order_by('id')
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
@api_view(['PUT'])
def handleImageEdit(request):
     if request.method == 'PUT':
        try:
            data = json.loads(request.body)  # Parse the JSON array from the request body
            id = request.data.get('id')
            isSelect = request.data.get('isSelect')
            if id and isSelect is not None:
                imgObj = Image.objects.get(id=id)
                imgObj.isSelect = isSelect
                imgObj.save()
                
                image_serializer = ImageSerializer(imgObj).data
                return  Response({'success': True, 'message':'Image Edit Successful','data':image_serializer, 'status': status.HTTP_200_OK})
            else:
                return Response({'message': 'Data missing from request'}, status=400)
            
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data in the request body'}, status=400);
        except Exception as e:
            return  Response({'success': False, 'message':{e}, 'status': 500})