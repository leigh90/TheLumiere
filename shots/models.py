# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 250)
    location_logo = CloudinaryField(blank=True)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
    
    def __str__(self): 
        return self.location
    
    
class Category(models.Model):
    category = models.CharField(max_length = 250) 
    category_logo = CloudinaryField()

    def __str__(self):
        return self.category

class Image(models.Model):
    image = CloudinaryField()
    image_name= models.CharField(max_length = 250)
    image_location=models.ForeignKey(Location)
    image_category=models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        Image.image_list.append(self)
    
    def delete_image(self):
        Image.image_list.remove(self)

    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__icontains=search_term)
        return images

#     @classmethod
#    def search_image(cls, category):
#        images = cls.objects.filter(image_description__icontains=category)

#        return images

    # @classmethod
    # def search_by_name(cls,search_term):
    #     images = cls.objects.filter(image_name__icontains = search_term)
    #     return images

    @classmethod
    def filter_by_location(cls,location):
        locationimages = Image.objects.filter(image_location__location=location).all()
        return locationimages
    

    # @classmethod
    # def filter_by_category(cls,category):
    #     locations = cls.objects.filter(image_category__icontains = image_Category)
    #     return images
