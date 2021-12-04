from django.db.models.aggregates import Avg
from django.shortcuts import render
from intexApp.models import PdPrescribersCredentials, PdPrescriber, PdDrugs, PdTriple

# Create your views here.

def indexPageView(request) :
    return render(request, 'intexApp/index.html')

def drugPageView(request) :
    data = PdDrugs.objects.all()
    context = {
        "drug" : data,

    }
    return render(request, 'intexApp/layout-sidenav-light.html', context)

def singleDrugPageView(request, drugname) :
    data = PdDrugs.objects.get(drugname = drugname)
    presdata = PdTriple.objects.filter(drugname = drugname) 

    #presdata = PdTriple.objects.raw(f"select id, prescriberid, drugname, qty from pd_triple order by drugname, qty desc limit 10;")
    context = {
        "drug" : data,
        "pres" : presdata
    }
    return render(request, 'intexApp/singleDrug.html', context)

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
    data = PdPrescriber.objects.raw(f"select * from pd_prescriber order by npi")
    context = {
        "pres" : data,

    }
    
    return render(request, 'intexApp/layout-static.html', context)

def singlePrescriberPageView(request, npi) :
    data = PdPrescriber.objects.get(npi = npi)
    drugdata = PdTriple.objects.filter(prescriberid = npi)
    avg = PdTriple.objects.filter(prescriberid = npi)
    avg = Avg(avg.values)
    #avg = str(avg)
    context = {
        "pres" : data,
        "drug" : drugdata,
        #"avg" : avg,
    }
    return render(request, 'intexApp/singlePrescriber.html', context)

def addPrescriberPageView(request) :
    if request.method == "POST" : 
        prescriber = PdPrescriber()
        prescriber.npi = request.POST['npi']
        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        prescriber.state = request.POST['state']
        prescriber.specialty = request.POST['specialty']
        prescriber.isopioidprescriber = request.POST['isopioidprescriber']
        prescriber.totalprescriptions = request.POST['totalprescriptions']

        prescriber.save()
        return prescriberPageView(request)
    else :
        return render(request, 'intexApp/addPrescriber.html')

def deletePrescriberPageView(request, npifr) :
    data = PdPrescriber.objects.get(npi = npifr)

    data.delete()

    return prescriberPageView(request)

def updatePresPageView(request):
    if request.method == 'POST' :
        npi = request.POST['npi']

        customer = PdPrescriber.objects.get(npi=npi)

        customer.fname = request.POST['fname']
        customer.lname = request.POST['lname']
        customer.gender = request.POST['gender']
        customer.state = request.POST['state']
        customer.specialty = request.POST['specialty']
        customer.isopioidprescriber = request.POST['isopioidprescriber']
        customer.totalprescriptions = request.POST['totalprescriptions']

        customer.save()

    return prescriberPageView(request)


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


