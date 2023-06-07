from django.shortcuts import render

from food.models import Food

def index(request):
    food = Food.objects.all()
    return render(request, 'core/index.html', {'food': food})