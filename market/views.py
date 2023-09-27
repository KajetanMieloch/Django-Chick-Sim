from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import UserProfile, BuildingLevel
from django.contrib import messages
from market.models import Shopping_item

@login_required
def index(request):
    
    shoping_items = Shopping_item.objects.all()
    
    return render(request, 'market/index.html', {
        'shoping_items': shoping_items
        })


@login_required
def buy_sell_eggs(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        print(buy_sell_eggs)
        if action == 'buy':
            user_profile = UserProfile.objects.get(user=request.user)
            money = user_profile.money
            egg = user_profile.egg
            ammount = int(request.POST.get('eggs'))
            if money >= ammount:
                user_profile.money -= ammount
                user_profile.egg += ammount
                user_profile.save()
                messages.success(request, f'{ammount} eggs bought successfully')
            else:
                messages.error(request, f'Not enough money to buy {ammount} eggs')
        elif action == 'sell':
            user_profile = UserProfile.objects.get(user=request.user)
            egg = user_profile.egg
            ammount = int(request.POST.get('eggs'))
            if egg >= ammount:
                user_profile.egg -= ammount
                user_profile.money += ammount
                user_profile.save()
                messages.success(request, f'{ammount} eggs sold successfully')
            else:
                messages.error(request, f'Not enough eggs to sell {ammount}')
        else:
            print(request.POST)
    return redirect('market:index')