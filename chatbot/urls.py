from django.urls import path
from . import views

urlpatterns = [
    path('', views.chtbot, name='chatbot')
]