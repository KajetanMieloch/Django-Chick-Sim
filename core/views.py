from django.shortcuts import render, redirect
from user.models import UserProfile
from buildings.models import Building

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
                
            return redirect('core:login')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })
    
def soon(request):
    return render(request, 'core/soon.html')