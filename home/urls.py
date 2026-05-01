from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('preowned-cars/', views.preowned_cars, name='preowned_cars'),
    path('other-services/', views.other_services, name='other_services'),
]
