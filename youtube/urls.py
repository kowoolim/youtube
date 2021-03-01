from django.urls import path
from youtube import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.index, name='index'),
    path('predict',views.predict, name='predict'),
]