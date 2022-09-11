from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Option(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    isCheckd = models.BooleanField(False)
    
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.OneToOneField(Option, on_delete=models.CASCADE)
    isCorrect = models.BooleanField(False)
    
    