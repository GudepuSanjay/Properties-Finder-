from django.shortcuts import render
from properties.models import Property
from django.db.models import Q 
# Create your views here.
def buying_properties(request):
    properties=Property.objects.filter(type_property='Sale')

    location=request.GET.get('location')
    property_type=request.GET.get('property_type')
    status=request.GET.get('status')

    flat_count = properties.filter(property_type='Flat').count()
    villa_count = properties.filter(property_type='Villa').count()
    plot_count = properties.filter(property_type='Plot').count()
    commercial_count = properties.filter(property_type='Commercial').count()

    if location:
        properties=properties.filter(Q(locations__icontains=location)|Q(near_location__icontains=location))
    
    if property_type:
        properties=properties.filter(property_type=property_type)
    
    if status:
        properties=properties.filter(status=status)


    context = {
        'properties': properties,
        'flat_count': flat_count,
        'villa_count': villa_count,
        'plot_count': plot_count,
        'commercial_count': commercial_count
    }
    return render(request,'accounts/buyers.html',context)