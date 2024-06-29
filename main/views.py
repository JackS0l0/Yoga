from django.shortcuts import render
from .models import Cover
def home(request):
    data={
        'title':'eStore',
        'cover':Cover.objects.all(),
    }
    return render(request,'index.html',data)