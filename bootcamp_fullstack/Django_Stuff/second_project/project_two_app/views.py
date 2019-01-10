from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.

def index(request):
    index_dict = {'index_dict':"lets do somethinggggg!"}
    return render(request,'second_project_app/index.html',context=index_dict)

def users(request):
    usr_list = Users.objects.order_by('first_name')
    usr_dict = {"users":usr_list}
    return render(request,'second_project_app/users.html',usr_dict)
