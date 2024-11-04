from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pages.choices import price_choices,state_choices,bedroom_choices

# Create your views here.

def listings(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,pk=None):
    listing = get_object_or_404(Listing,pk=pk)
    context = {
        'listing':listing,
        'photo_range': 6
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    # Keywords search
    
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City search
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    
    # State Search
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            
    # Bedrooms Search
    
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            
    # Price Search
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    context = {
        'listings': queryset_list,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'values': request.GET
    }
    return render(request,'listings/search.html',context)