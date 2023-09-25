from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Building
from django.http import HttpResponse

from buildings.models import Building

@login_required
def index(request):
    
    buildings = Building.objects.all()
    user_profile = request.user.userprofile
    
    return render(request, 'buildings/index.html', {
        "buildings": buildings,
        "user_profile": user_profile,
    })


@login_required
def build_building(request):  
    if request.method == 'POST':
        building_id = request.POST.get('building_id')
        building = Building.objects.get(id=building_id)
        user_profile = request.user.userprofile
        user_profile.buildings.add(building)
        building.owned = True
        building.save()
        return redirect('buildings:index')
    else:
        return redirect('buildings:index')
