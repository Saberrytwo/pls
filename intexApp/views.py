from django.shortcuts import render

# Create your views here.

def prescriberPageView(request) :
    return render(request, 'intexApp/index.html')

def drugPageView(request) :
    return render(request, 'intexApp/charts.html')

def analysesPageView(request) :
    return render(request, 'intexApp/tables.html')
