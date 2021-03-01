from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('onRewrite', views.onRewrite, name='onRewrite'),
]