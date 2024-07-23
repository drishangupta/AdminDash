from django.shortcuts import render
from .models import Datas
# Create your views here.
def home(request):
    return "<p>Hi</p>"