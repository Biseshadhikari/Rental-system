from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('details/<int:id>',views.detailView,name='details'),
    
]