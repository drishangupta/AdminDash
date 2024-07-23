from django.urls import path 
from . import views
urlpatterns = [
    path("Page",views.home,name='home')
]
