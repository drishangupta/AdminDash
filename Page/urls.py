from django.urls import include,path 
from . import views

urlpatterns = [
    path("Page",views.home,name='home'),
    
]
