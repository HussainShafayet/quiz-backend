from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Category, Question, Option, Answer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields ='__all__'