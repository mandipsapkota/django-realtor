from django.shortcuts import render , redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.

# CRUD - create , retrieve , update , delete , list

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings" : listings 
    }
    return render(request, "listings.html" , context)

# Retrieve 
def listing_retrieve(request , pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing" : listing
    }
    return render(request , "listing.html" , context)

# Ceating and updating need forms 
def listing_create(request):
    form = ListingForm()
    print(request.POST)
    if request.method == "POST":
        form = ListingForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {
        "form":form
    }
    return render(request,"listing_create.html",context)

def listing_update(request , pk):
    listing = Listing.objects.get(id = pk)
    form = ListingForm(instance = listing)

    if request.method == "POST":
        form = ListingForm(request.POST , instance = listing , files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {
        "form":form
    }
    return render(request,"listing_update.html",context)

def listing_delete(listing , pk):
    listing = Listing.objects.get(id = pk)
    listing.delete()
    return redirect("/")