from django.shortcuts import render

# Create your views here.

def listings(request):
    return render(request,'listings/listings.html')

def listing(request,pk=None):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')