from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'index.html',date_dict)

def help(request):
    help_dict = {'help_me':"lets do somethinggggg!"}
    return render(request,'help.html',context=help_dict)
