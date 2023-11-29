from django.urls import path
#from .views import *
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('booking/',views.booking,name="booking"),
    path('doctors/',views.doctors,name="doctors"),
    path('contacts/',views.contact,name="contacts"),
    path('department/',views.department,name="department"),
]