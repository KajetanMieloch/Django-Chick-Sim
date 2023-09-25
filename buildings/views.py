from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from buildings.models import Building
from user.models import UserProfile, BuildingLevel
from django.contrib import messages


@login_required
def index(request):
    user_profile = UserProfile.objects.get(user=request.user)
    buildings = Building.objects.all()
    building_levels = BuildingLevel.objects.filter(user_profile=user_profile)
    building_levels_dict = {bl.building_id: bl.level for bl in building_levels}


    
    context = {
        'user_profile': user_profile,
        'buildings': buildings,
        'building_levels': building_levels_dict
    }
    return render(request, 'buildings/index.html', context)


@login_required
def upgrade_building(request):
    if request.method == 'POST':
        building_id = request.POST.get('building_id')
        user_profile = UserProfile.objects.get(user=request.user)
        building_level = BuildingLevel.objects.get(user_profile=user_profile, building_id=building_id)
        building = building_level.building
        building_upgrade_cost = (building_level.level+building.cost)*180
        if user_profile.money >= building_upgrade_cost:
            user_profile.money -= building_upgrade_cost
            building_level.level += 1
            building_level.save()
            user_profile.save()
            messages.success(request, f'{building.name} upgraded to level {building_level.level}')
        else:
            messages.error(request, f'Not enough money to upgrade {building.name}')
    return redirect('buildings:index')


@login_required
def build_building(request):  
    if request.method == 'POST':
        building_id = request.POST.get('building_id')
        building = Building.objects.get(id=building_id)
        user_profile = request.user.userprofile
        if user_profile.money >= building.cost:
            user_profile.money -= building.cost
            user_profile.buildings.add(building)
            building.owned = True
            building.save()
            user_profile.save()
            messages.success(request, f'{building.name} built successfully')
        else:
            messages.error(request, f'Not enough money to build {building.name}')
        return redirect('buildings:index')
    else:
        return redirect('buildings:index')