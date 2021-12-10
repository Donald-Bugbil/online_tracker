from django.shortcuts import render

# Create your views here.

def Home_page(request):
    template = "pages/home.html"

    return render(request, template)