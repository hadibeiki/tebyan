from django.urls import path

from registerEatekaf import views

urlpatterns = [
    path('alldata/<str:id>/', views.allData, name='alldata'),
    path('alldatamosque/<str:id>/', views.allDataMosque, name='alldatamosque'),
    path('signup/', views.signupview, name='signupurl'),
    path('report/<str:id>/', views.reportview, name='reqporturl'),
    path('gotobank/<str:melicode>/<str:mosque>/', views.go_to_gateway_view, name='gotogetway'),
    path('callback/<str:id>/', views.callback_gateway_view, name="callback-gateway"),
    path('success/<str:id>/', views.successView, name="successPay")
]