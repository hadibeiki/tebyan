from django.urls import path

from contact import views

urlpatterns = [
    path('eatekaf/', views.viewindex, name='EatekafIndex'),
    path('addcontact/<str:melicode>/', views.viewaddcontact, name='urladdcontact'),
    path('verify/', views.Vverify, name='verify'),
    path('delete/<str:melicode>', views.deletecontact, name='deletecontact'),
    path('confirm/<str:melicode>', views.confirmcontact, name='confirmcontact'),

]