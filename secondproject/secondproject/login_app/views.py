from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    return render(request, 'login_app/HomePage.html')