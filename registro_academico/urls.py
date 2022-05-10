from django.urls import path, re_path
from registro_academico import views

urlpatterns = [
	path('', views.index, name='index'),
]