from django.shortcuts import render
from .models import Datas
# Create your views here.
def home(request):
    return render(request,Datas,{"fields":Datas.name})