from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from properties.models import Property
from .forms import SignupForm,LoginForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from properties import views
from buying_properties.views import buying_properties
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            role=request.POST.get('role')
            
            Profile.objects.create(user=user,role=role)
            messages.success(request,'Account Created Successfully!')

            if role=='agent':
                return redirect('agent_dashboard')
            else:
                return redirect('user_dashboard')
            
            # return redirect('login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)

            role=user.profile.role
            if role=='agent':
                return redirect('agent_dashboard')
            else:
                # properties=Property.objects.filter(status='Available')
                # return render(request,'user_dashboard.html',{'properties':properties})
                return redirect('user_dashboard')
            # messages.success(request,'Logged in successfully!')
            # return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.info(request,'Logged out!')
    return redirect('login')

@login_required
def agent_dashboard(request):
   properties = Property.objects.filter(agent=request.user)
   return render(request,'agent_dashboard.html',{'properties':properties})
    

@login_required
def user_dashboard(request):
    properties=Property.objects.all()
    location=request.GET.get('location')
    property_type=request.GET.get('property_type')
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')
    type_property=request.GET.get('type_property')
    status=request.GET.get('status')

    min_bedrooms=request.GET.get('min_bedrooms')
    min_bathrooms=request.GET.get('min_bathrooms')
    min_sqft=request.GET.get('min_sqft')
    max_sqft=request.GET.get('max_sqft')
    amenities=request.GET.get('amenities')


    if location:
        properties=properties.filter(Q(locations__icontains=location)|Q(near_location__icontains=location))

    if property_type:
        properties=properties.filter(property_type=property_type)

    if min_price:
        try:
            properties=properties.filter(price__gte=float(min_price))
        except(ValueError,TypeError):
            pass

    if max_price:
        try:
            properties=properties.filter(price__lte=float(max_price))
        except (ValueError,TypeError):
            pass

    if type_property:
        properties=properties.filter(type_property=type_property)
        
    if status:
        properties=properties.filter(status=status)
    
    if min_bedrooms:
        try:
            properties=properties.filter(bedrooms__gte=int(min_bedrooms))
        except(ValueError,TypeError):
            pass
    
    if min_bathrooms:
        try:
            properties=properties.filter(bathrooms__gte=int(min_bathrooms))
        except(TypeError,ValueError):
            pass
    
    if min_sqft:
        try:
            properties=properties.filter(squarefeets__gte=int(max_sqft))
        except(ValueError,TypeError):
            pass
    
    if max_sqft:
        try:
            properties=properties.filter(squarefeets__lte=int(max_sqft))
        except(ValueError,TypeError):
            pass

    if amenities:
        amenities_list = amenities.split(',')
        # Create Q objects for each selected amenity
        
        amenity_filters = Q()
        for amenity in amenities_list:
            # For MultiSelectField, we need to check if the amenity is in the list
            amenity_filters |= Q(amenities__contains=amenity)
        properties = properties.filter(amenity_filters)

    return render(request,"user_dashboard.html",{"properties":properties})
    





@login_required
def update_profile_agent(request):
    user_form=UserUpdateForm(instance=request.user)
    profile_form=ProfileUpdateForm(instance=request.user.profile)

    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
             user_form.save()
             profile_form.save()
             messages.success(request,"Profile Updated Succesfully!")
             return redirect('agent_dashboard')
    
    return render(request,'accounts/update_profile_agent.html',{'user_form':user_form,'profile_form':profile_form})


@login_required
def update_profile_user(request):
    user_form=UserUpdateForm(instance=request.user)
    profile_form=ProfileUpdateForm(instance=request.user.profile)

    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
             user_form.save()
             profile_form.save()
             messages.success(request,"Profile Updated Succesfully!")
             return redirect('user_dashboard')
    
    return render(request,'accounts/update_profile_user.html',{'user_form':user_form,'profile_form':profile_form})



