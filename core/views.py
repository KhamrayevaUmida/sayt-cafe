from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def fast_food(request):
    return render(request, 'fast_food.html')
