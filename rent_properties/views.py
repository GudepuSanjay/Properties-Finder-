from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from properties.models import Property  # Assuming your Property model is in this app

def rent_properties(request):
    # Get all rental properties
    properties = Property.objects.filter(type_property='Rent')
    
    # Get filter parameters from request
    location = request.GET.get('location')
    property_type = request.GET.get('property_type')
    
    # Apply filters if provided
    if location:
        properties = properties.filter(
            Q(locations__icontains=location) | 
            Q(near_location__icontains=location)
        )
    
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    # Pagination - 9 properties per page
    # paginator = Paginator(properties, 9)
    # page = request.GET.get('page')
    
    # try:
    #     properties_page = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page
    #     properties_page = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range, deliver last page of results
    #     properties_page = paginator.page(paginator.num_pages)
    
    context = {
        'properties': properties,
    }
    
    return render(request, 'accounts/rent.html', context)