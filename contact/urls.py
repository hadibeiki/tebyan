from django.urls import path

from contact import views

urlpatterns = [
    path('', views.viewindex, name='index'),
    path('addoreditcontact/<str:melicode>/', views.viewaddoreditcontact, name='urladdoreditcontact'),
    path('verify/', views.Vverify, name='verify'),
]