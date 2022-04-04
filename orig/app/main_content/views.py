from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def creator_view(request):
    return render(request, 'creator.html')

def login_view(request):
    return render(request, 'login.html')

def team_view(request):
    return render(request, 'team.html')