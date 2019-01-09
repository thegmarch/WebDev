from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    my_dict = {'insert_me':"lets do somethinggggg!"}
    return render(request,'index.html',context=my_dict)

def help(request):
    help_dict = {'help_me':"lets do somethinggggg!"}
    return render(request,'help.html',context=help_dict)
