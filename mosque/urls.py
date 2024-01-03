from django.urls import path

from mosque import views

urlpatterns = [
    path('selectmosqu/', views.selectMosque, name='selectMosque'),
    path('mosquedetail/', views.mosquedetail, name='detailMosque'),
    path('mosquedit/<str:id>/', views.mosquedit, name='editMosque'),
]