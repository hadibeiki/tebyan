from django.urls import path

from registerEatekaf import views

urlpatterns = [
    path('alldata/<str:id>/', views.allData, name='alldata'),
    path('signup/', views.signupview, name='signupurl'),
    path('report/<str:id>/', views.reportview, name='reqporturl'),
    path('gotobank/<str:id>/<str:melicode>/', views.go_to_gateway_view, name='gotogetway'),
    path('callback/<str:melicode>/<str:id>/', views.callback_gateway_view, name="callback-gateway"),
    path('success/<str:melicode>/', views.successView, name="successPay")
]