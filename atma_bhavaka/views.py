# atma_bhavaka/views.py

from django.shortcuts import render
from content.models import PageContent, ContactInfo, PackagePrice

def home_view(request):
    quote = PageContent.objects.filter(page='home', section_key='quote', is_active=True).first()
    context = {
        'quote': quote,
    }
    return render(request, 'home.html', context)

def about_view(request):
    about_content = PageContent.objects.filter(page='about', is_active=True).order_by('order')
    context = {
        'about_content': about_content,
    }
    return render(request, 'about.html', context)

def book_view(request):
    atma_intro = PageContent.objects.filter(page='book', section_key='atma_bhavaka_intro', is_active=True).first()
    stemexpressie_intro = PageContent.objects.filter(page='book', section_key='stemexpressie_intro', is_active=True).first()
    packages = PackagePrice.objects.filter(is_active=True).order_by('order')
    context = {
        'atma_intro': atma_intro,
        'stemexpressie_intro': stemexpressie_intro,
        'packages': packages,
    }
    return render(request, 'book.html', context)

def learn_view(request):
    learn_sections = PageContent.objects.filter(page='learn', is_active=True).order_by('order')
    context = {
        'learn_sections': learn_sections,
    }
    return render(request, 'learn.html', context)

# def gallery_view(request):
#     return render(request, 'gallery.html')