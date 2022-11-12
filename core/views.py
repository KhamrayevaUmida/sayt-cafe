from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def fast_food(request):
    return render(request, 'fast_food.html')

def pizza(request):
    return render(request, 'pizza.html')

def coffee(request):
    return render(request, 'coffee.html')

def drink(request):
    return render(request, 'drink.html')

def help(request):
    return render(request, 'help.html')

def order(request):
    return render(request, 'order.html')
