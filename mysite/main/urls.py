from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shops', views.about, name='about'),
    path('catalog', views.catalog, name='catalog')
]
