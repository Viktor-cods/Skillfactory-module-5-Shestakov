from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('author_list',AuthorList.as_view()),
    path('news_list/',index,name='index'),
    path('new/<str:slug>',default,name='default'),
    path('post/<int:pk>/',Post.as_view()),
]