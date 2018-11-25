from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single', views.single, name='single'), #solo para tests porque single no sera, solo es el modelo. luego ira la url con la fecha + nombre
    path('member', views.member, name='member'),
    #path('blog', views.blog, name='blog'),
]