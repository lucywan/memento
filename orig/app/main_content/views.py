from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def login_view(request):
    return render(request, 'login.html')

def team_view(request):
    return render(request, 'team.html')

def profile_view(request):
    return render(request, 'profile.html')

from creator_forms.models import SubmitNFTModel

def my_nft_view(request):
    context = {}
    u = request.user
    pending = SubmitNFTModel.objects.filter(username = u)
    context["nft"] = pending
    context["message"] = ""
    return render(request, 'my_nft.html', context)