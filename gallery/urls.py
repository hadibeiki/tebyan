from django.urls import path

from gallery import views

urlpatterns = [
    path('selectgallery/<str:id>/', views.selectgallery, name='selectgallery'),
    path('addgallery/', views.addgallery, name='addgalleryurl'),
]