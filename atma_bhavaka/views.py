# atma_bhavaka/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def book_view(request):
    return render(request, 'book.html')

def learn_view(request):
    return render(request, 'learn.html')

# def gallery_view(request):
#     return render(request, 'gallery.html')