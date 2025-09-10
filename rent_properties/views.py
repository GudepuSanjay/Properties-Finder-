from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from properties.models import Property  

def rent_properties(request):
    
    properties = Property.objects.filter(type_property='Rent')
    
    
    location = request.GET.get('location')
    property_type = request.GET.get('property_type')
    
    
    if location:
        properties = properties.filter(
            Q(locations__icontains=location) | 
            Q(near_location__icontains=location)
        )
    
    if property_type:
        properties = properties.filter(property_type=property_type)

    context = {
        'properties': properties,
    }
    
    return render(request, 'accounts/rent.html', context)