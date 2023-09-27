from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Department, Chicken
from user.models import UserProfile
from django.http import JsonResponse

@login_required
def index(request):
    
    departments = Department.objects.all()
    

    
    return render(request, 'dashboard/index.html', {
        'departments': departments,
    })

@login_required
def chart_data(request):
    
    user_profile = UserProfile.objects.get(user=request.user)
    
    return JsonResponse({
        'egg_amount': user_profile.int_array,
    })
