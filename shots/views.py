# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from . models import Location, Category, Image
import cloudinary
# Create your views here.

def index(request):
    '''
    Returns the home page with all the images
    '''
    images = Image.objects.all()
    imagelocation = Location.objects.all()
    imagecategory = Category.objects.all()
    locations = Location.get_locations()
    print(locations)

    args = {'images': images, 'imagelocation':imagelocation, 'imagecategory':imagecategory }
    
    return render(request, 'index.html', args)
    

def allcategories(request):
    '''
    Returns a list of all the image categories available
    '''
    allcategories = Category.objects.all()
    return render (request, 'categories.html',locals())

def locations(request):
    '''
    Returns a list of the location tagged to the images
    '''
    alllocations = Location.objects.all()
    return render (request, 'areas.html',locals())

def nairobiimages(request):
    '''
    Returns a list of all images from Nairobi
    '''
    images = Image.objects.filter(image_location__location='Nairobi')
    return render(request, 'nairobi.html',locals())

def dianiimages(request):
    '''
    Returns a list of all the images from Diani
    '''
    images = Image.objects.filter(image_location__location='Diani')
    return render(request, 'diani.html',locals())

def search(request):
    query = request.GET.get('q')
    if query:
        images = Image.objects.filter(Q(image_category__category__icontains=query))
    else:
        images = Image.objects.all()
    return render(request,'search.html',locals())








# def search(request):
#     if 'image' in request.GET and request.GET["image"]:
#         category = request.GET.get('image')
#         searched_images = Image.search_by_category(image_category)
#         message = f"{category}"
#         args = {"images": searched_images}
#         return render(request, "search.html", args)
#     else:
#         message = "You haven't searched for any term"
#         return render(request, "search.html", {"message":message})

# def search_by_category(request):
#     query = request.GET.get('q')
#     results = Image.objects.filter(Q(image__image_category__icontains=query))
#     return render(request,'search.html',locals())

# def search_by_category(request):
#     query = request.GET.get('q')
#     result = cloudinary.Search()
#     return render(request,'search.html',locals())


# result = cloudinary.Search()\
#   .expression('cat')\
#   .with_field('context')\
#   .with_field('tags')\
#   .max_results('10')\
#   .execute()


 
# def display_by_category(request):
#     images = Image.image_category()
#     args = {'images': images}
#     return render(request, 'categories.html', args)

# def display_by_location(request):
#     images = Image.image_location()
#     args = {'images':images}
#     return render(request, 'areas.html', args)