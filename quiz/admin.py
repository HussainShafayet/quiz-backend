from tkinter.messagebox import QUESTION
from django.contrib import admin
from .models import Answer, Category,Question,Option
# Register your models here.

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
