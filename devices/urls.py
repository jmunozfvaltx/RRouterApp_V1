#urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('verify/', views.verify, name='verify'),
    path('results/', views.results, name='results'),

]