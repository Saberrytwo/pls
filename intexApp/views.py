from django.shortcuts import render

# Create your views here.

def indexPageView(request) :
    return render(request, 'intexApp/index.html')

def drugPageView(request) :
    return render(request, 'intexApp/layout-sidenav-light.html')

def prescriberPageView(request) :
    return render(request, 'intexApp/layout-static.html')
