from django.urls import path
from .views import index,detail

urlpatterns = [
    path('simleapp_new/',index,name='index'),
    path('simpl/<str:slug>',detail,name='detail')
]