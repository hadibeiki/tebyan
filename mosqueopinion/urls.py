from django.urls import path

from mosqueopinion import views

urlpatterns = [
    path('mosqueopinion/', views.mosqueOpinion, name='mosqueopinion'),
]