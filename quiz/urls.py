from django.urls import path
from  . import views 
urlpatterns = [
    path('quiz.categorycreataorget',views.handleCategory, name='quiz.categorycreataorget')
]
 