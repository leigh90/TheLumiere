from django.conf.urls import url
from . import views
from .views import search_by_category, nairobiimages, dianiimages,locations

app_name = 'shots'

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^allcategories/',views.allcategories, name='allcategories'),
    url(r'^locations/',views.locations, name='alllocations'),
    url(r'^nairobi/', views.nairobiimages, name = 'nairobi' ),
    url(r'^diani/', views.dianiimages, name = 'diani' ),
    url(r'^search/', views.search_by_category, name = 'search'),
    
]