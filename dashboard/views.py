from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Department, Chicken

@login_required
def index(request):
    
    departments = Department.objects.all()
    
    return render(request, 'dashboard/index.html', {
        'departments': departments,
    })