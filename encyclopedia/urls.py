from django.urls import path

from . import views

urlpatterns = [
    path("", views.whoami, name='whoami'),
    path("allfiles", views.index, name="index"),
    path('search', views.search, name='search'),
    path('edited', views.edited, name='edited'),
    path('newpage', views.newpage, name='newpage'),
    path('addpage', views.add, name='addpage'),
    path('random', views.random, name='random'),
    path('page/<str:name>', views.getentry, name='getentry'),
    path('image/<str:imgid>', views.image, name='image'),
    path('fileupload', views.storeAndProcessFile, name='storeandprocessfile')
    ]
