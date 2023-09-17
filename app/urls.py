from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.home),
    path('register',views.register ,name='hi'),
    path('todo',views.todo),
    
]
