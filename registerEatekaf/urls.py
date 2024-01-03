from django.urls import path

from registerEatekaf import views

urlpatterns = [
    path('alldata/<str:id>/', views.allData, name='alldata'),
    path('signup/', views.signupview, name='signupurl'),
    path('report/<str:id>/', views.reportview, name='reqporturl'),
    path('callback/', views.callback_gateway_view, name="callback-gateway"),
    path('gotobank/', views.go_to_gateway_view, name='gotogetway')
]