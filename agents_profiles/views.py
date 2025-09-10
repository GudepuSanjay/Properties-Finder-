from django.shortcuts import render
from django.db.models import Q
from accounts.models import Profile

def agents_profiles(request):
    
    agents = Profile.objects.filter(role='agent').select_related('user')
    
    search_query = request.GET.get('search', '')
    
    # Search filter 
    if search_query:
        agents = agents.filter(
            Q(user__username__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(specialization__icontains=search_query) |
            Q(property_types__icontains=search_query)
        )
    
    
    filter_type = request.GET.get('filter', '')
    
    if filter_type == 'top_rated':
        agents = agents.filter(rating__gte=4.0).order_by('-rating')
    elif filter_type == 'most_experienced':
        agents = agents.order_by('-years_experience')
    
    context = {
        'agents': agents,
        'search_query': search_query,
        'current_filter': filter_type
    }
    
    return render(request, 'accounts/agents.html', context)