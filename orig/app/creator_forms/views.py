# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .forms import SubmitNFTForm
from .models import SubmitNFTModel



def create_view(request):
    form = SubmitNFTForm(request.POST or None, request.FILES or None)
    context = {}
    if request.method == "POST":
        # pending = SubmitNFTModel.objects.all()
        # context["pending"] = pending
        if form.is_valid():
            # form.username = request.username
            form.save()
            message = "NFT successfully submitted!"
            context["message"]: message
            context["form"] = form
            return redirect('my_nft')
        # else:
        #     message = "NFT submission error. Please try again."
        #     return render(request, 'my_nft.html', context)
    context["form"] = form
    return render(request, 'creator.html', context)


    # nft = SubmitNFTForm(request.POST or None, request.FILES or None)
    # context = {}
    # if nft.is_valid():
    #     nft.username = request.user.username
    #     nft.save()
    #     message = "NFT successfully submitted!"
    # else:
    #     message = "NFT submission error. Please try again."
    # context["message"]: message
    # pending = SubmitNFTModel.objects.all()
    # context["pending"] = pending
    # context['form'] = nft
    # return render(request, 'creator.html', context)

