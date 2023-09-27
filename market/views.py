from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import UserProfile, BuildingLevel
from django.contrib import messages
from market.models import Shopping_item

@login_required
def index(request):
    
    shoping_items = Shopping_item.objects.all()
    
    return render(request, 'market/index.html', {
        'shoping_items': shoping_items,
        })


@login_required
def buy_sell_eggs(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        item_name = request.POST.get('item_name')
        action = request.POST.get('action')
        
        item = getattr(user_profile, item_name)

        if action == 'buy':

            money = user_profile.money
            ammount = int(request.POST.get('eggs'))
            cost_buy = Shopping_item.objects.get(name=item_name).costbuy
            
            if money >= ammount:
                setattr(user_profile, item_name, item + ammount)
                user_profile.money -= ammount * cost_buy
                user_profile.save()
                messages.success(request, f'{ammount} {item_name} bought successfully')
            else:
                messages.error(request, f'Not enough money to buy {ammount} {item_name}')
        elif action == 'sell':
            ammount = int(request.POST.get('eggs'))
            cost_sell = Shopping_item.objects.get(name=item_name).costsell
            
            if item >= ammount:
                setattr(user_profile, item_name, item - ammount)
                user_profile.money += ammount * cost_sell
                user_profile.save()
                messages.success(request, f'{ammount} {item_name} sold successfully')
            else:
                messages.error(request, f'Not enough {item_name} to sell {ammount}')
        else:
            print(request.POST)
    return redirect('market:index')