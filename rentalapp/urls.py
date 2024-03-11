from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('update/<int:id>',views.update,name='update')
    
]