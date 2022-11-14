from django.shortcuts import render

def fast_food(request):
    return render(request, 'backend/fast_food.html')

def pizza(request):
    return render(request, 'backend/pizza.html')

def coffee(request):
    return render(request, 'backend/coffee.html')

def drink(request):
    return render(request, 'backend/drink.html')

def help(request):
    return render(request, 'backend/help.html')

def order(request):
    return render(request, 'backend/order.html')

