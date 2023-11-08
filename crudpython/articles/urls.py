from django.urls import path
from .import views

urlpatterns= [
    path('', views.article_data),
    path('about/',views.article_about),
]