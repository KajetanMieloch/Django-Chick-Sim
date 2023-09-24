from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from buildings.models import Building

@login_required
def index(request):
    
    buildings = Building.objects.all()
    
    return render(request, 'buildings/index.html', {
        "buildings": buildings,
    })
