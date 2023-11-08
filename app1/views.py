from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def siva(request):
    return HttpResponse('<h1><marquee>hii siva anna how are you</h1></marquee>')