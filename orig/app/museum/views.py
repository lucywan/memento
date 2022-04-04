from django.shortcuts import render

# Create your views here.
def museum_view(request):
    return render(request, 'museum.html')
