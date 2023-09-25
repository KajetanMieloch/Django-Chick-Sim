from django.shortcuts import render, redirect
from user.models import UserProfile, BuildingLevel
from buildings.models import Building
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            user_profile = UserProfile.objects.create(user=form.instance)
            user_profile.buildings.set(Building.objects.all()[:1])
            
            BuildingLevel.objects.bulk_create([
                BuildingLevel(user_profile=user_profile, building=building)
                for building in Building.objects.all()
            ])
                
            return redirect('core:login')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })

@login_required
def live_data(request):
    
    user_profile = UserProfile.objects.get(user=request.user)
    
    return JsonResponse({
        'egg': user_profile.egg,
        'money': user_profile.money,
    })
    
def soon(request):
    return render(request, 'core/soon.html')