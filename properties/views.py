from django.shortcuts import get_object_or_404, render,redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required

from agents_profiles import views
# Create your views here.

@login_required
def property_list(request):
    properties=Property.objects.filter(status='Available')
    return render(request,'properties/property_list.html',{'properties':properties})

@login_required
def property_detail(request,pk):
    property_obj=get_object_or_404(Property,pk=pk)
    agents_obj=property_obj.agent
    return render(request,'properties/property_detail.html',{'properties':property_obj,'agent':agents_obj})

@login_required
def agent_property_list(request):
    agent_properties=Property.objects.filter(agent=request.user)
    return render(request,'agent_dashboard.html',{'properties':agent_properties})

@login_required
def add_property(request):
    if request.method=='POST':
        form=PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            property_obj=form.save(commit=False)
            property_obj.agent=request.user
            property_obj.save()
            return redirect('agent_property_list')
    else:
        form=PropertyForm()
    return render(request,'properties/add_property.html',{'form':form})