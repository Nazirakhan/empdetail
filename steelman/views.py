from django.shortcuts import render
from .models import empdata


def emdata(request):
    datas = empdata.objects.all()
    return render(request,'index.html',{'data':datas})