from django.conf.urls import url
from . import views
from .views import search_by_category

app_name = 'shots'

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^allcategories/',views.allcategories, name='allcategories'),
    url(r'^locations/',views.locations, name='alllocations'),
    url(r'^search/', views.search_by_category, name = 'search')
]