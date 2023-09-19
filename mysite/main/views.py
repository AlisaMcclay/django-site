from django.shortcuts import render
from .models import Shops, Books


def index(request):
    return render(request, 'main/index.html')


def about(request):
    shops = Shops.objects.all()
    return render(request, 'main/about.html', {'shops': shops})


def catalog(request):
    books = Books.objects.all()
    return render(request, 'main/catalog.html', {'books': books})
