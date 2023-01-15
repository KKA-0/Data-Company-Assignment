from django.shortcuts import render
from django.http import HttpResponse

#LOGIN FUNCTION
def LoginActivity(request):
    return render(request,"login.html")
#HOME FUNCTION
def home(request):
    return render(request,"index.html")