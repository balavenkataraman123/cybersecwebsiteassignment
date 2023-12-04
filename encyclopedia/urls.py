from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index1'),
    path("allfiles", views.index, name="index"),
    path('search', views.search, name='search'),
    path('edited', views.edited, name='edited'),
    path('newpage', views.newpage, name='newpage'),
    path('addpage', views.add, name='addpage'),
    path('random', views.random, name='random'),
    path('page/<str:name>', views.getentry, name='getentry'),
    path('image/<str:imgid>', views.image, name='image'),
    path('interractive/<str:name>', views.interractive, name='inter'),
    path('fileupload', views.storeAndProcessFile, name='storeandprocessfile'),
    path('getthumbnail/<str:entryname>', views.getThumbNail, name = 'getthumbnail')
    ]
