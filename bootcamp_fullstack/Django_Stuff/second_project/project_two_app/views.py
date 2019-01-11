from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Users
from .forms import NewUser
# Create your views here.

def index(request):
    return render(request,'second_project_app/index.html')

def users(request):
    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")
    return render(request,'second_project_app/users.html',{'form':form})
