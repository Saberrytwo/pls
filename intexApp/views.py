from django.shortcuts import render
from intexApp.models import PdPrescribersCredentials, PdPrescriber, PdDrugs, PdTriple

# Create your views here.

def indexPageView(request) :
    return render(request, 'intexApp/index.html')

def drugPageView(request) :
    data = PdDrugs.objects.all()
    context = {
        "drug" : data
    }
    return render(request, 'intexApp/layout-sidenav-light.html', context)

def searchDrugsPageView(request):
    if request.method == "POST":
        search_term = request.POST['search']
        results = (PdDrugs.objects.filter(drugname__istartswith=search_term) or PdDrugs.objects.filter(isopioid__istartswith=search_term))
        context = {
            "drug" : results
        }
        return render(request, 'intexApp/layout-sidenav-light.html', context)
    data = PdDrugs.objects.all()
    context = {
        "drug" : data
    }
    return render(request, 'intexApp/layout-sidenav-light.html', context)


def prescriberPageView(request) :
    data = PdPrescriber.objects.all()
    context = {
        "pres" : data
    }
    
    return render(request, 'intexApp/layout-static.html', context)

def searchPrescribersPageView(request):
    if request.method == "POST":
        search_term = request.POST['search']
        search_type = request.POST.get('type')
        if search_type == 'npi' :
            results = PdPrescriber.objects.filter(npi__istartswith=search_term)
        elif search_type == 'fname' :
            results = PdPrescriber.objects.filter(fname__istartswith=search_term)
        elif search_type == 'lname' :
            results = PdPrescriber.objects.filter(lname__istartswith=search_term)
        elif search_type == 'gender' :
            results = PdPrescriber.objects.filter(gender__istartswith=search_term)
        elif search_type == 'state' :
            results = PdPrescriber.objects.filter(state__istartswith=search_term)
        elif search_type == 'specialty' :
            results = PdPrescriber.objects.filter(specialty__istartswith=search_term)
        context = {
            "pres" : results
        }
        return render(request, 'intexApp/layout-static.html', context)

""" def updatePrescribersPageView(request) :
    if request.method == 'POST' :
        drugid = request.POST['drugid']

        drug = PdDrugs.objects.get(id=drugid)

        drug.drugname = request.POST['drugname']
        drug.isopioid = request.POST['isopioid']


        drug.save()

    return prescriberPageView(request) """
