from turtle import title
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Image
from .serializers import ImageSerializer
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
def handleImage(request):
    if request.method == 'GET':
        imgs = Image.objects.all()
        imgSerializer = ImageSerializer(imgs, many = True).data
        data=[]
        for q in imgSerializer:
            data.append(q)
        return Response({'success': True, 'data':data, 'status': status.HTTP_200_OK})
    elif request.method == 'POST' and request.FILES.get('file'):
        #image_name = request.POST.get('image_name', 'Untitled Image')
        image_name = request.FILES['file'].name
        is_select = request.POST.get('is_select', False)
        is_featured = request.POST.get('is_featured', False)

        image = Image(file=request.FILES['file'], image_name=image_name, isSelect=is_select, isFeatured=is_featured)
        image.save()
       
        return Response({'success': True, 'data':{}, 'status': status.HTTP_200_OK})
        pass