from django.urls import path
from  . import views 
urlpatterns = [
    path('createorgetquestion',views.hello, name='createorgetquestion')
]
 