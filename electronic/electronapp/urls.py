from django.urls import path
from . import views

urlpatterns = [
    path('',views.findproduct,name="findproduct"),
    path('searching.../<str:product>/',views.runingselenium,name = "runingselenium"),
    path("showdata/<str:product>/",views.showdata,name="showdata"),
]