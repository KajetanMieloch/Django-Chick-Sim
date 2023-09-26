from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from buildings.models import Building
from user.models import UserProfile, BuildingLevel
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def index(request):
    user_profile = UserProfile.objects.get(user=request.user)
    buildings = Building.objects.all()
    building_levels = BuildingLevel.objects.filter(user_profile=user_profile)
    building_levels_dict = {bl.building_id: bl.level for bl in building_levels}
    building_eggs_dict = {bl.building_id: bl.egg_in_storage for bl in building_levels}


    
    context = {
        'user_profile': user_profile,
        'buildings': buildings,
        'building_levels': building_levels_dict,
        'building_eggs': building_eggs_dict,
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
    
    
@login_required
@csrf_exempt  # Remove if you're handling CSRF tokens differently
def save_eggs(request):
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body.decode('utf-8'))
            id = data.get('id')
            content = data.get('content')

            # Process the data as needed (e.g., save it to the database)
            
            print(id, content)

            user_profile = UserProfile.objects.get(user=request.user)
            building_levels = BuildingLevel.objects.filter(user_profile=user_profile)
            building_eggs_dict = {bl.building_id: bl.egg_in_storage for bl in building_levels}
            
            building_eggs_dict.update({int(id): int(content)})
            #Now save this new data
            for building_id, egg_count in building_eggs_dict.items():
                building_level = BuildingLevel.objects.get(user_profile=user_profile, building_id=building_id)
                building_level.egg_in_storage = egg_count
                building_level.save()
            

            return JsonResponse({'message': 'Data received and processed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)