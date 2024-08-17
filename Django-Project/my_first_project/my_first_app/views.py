from django.shortcuts import render
from .models import Car

# Create your views here.
def myView(request):
    car_list = Car.objects.all()  # Obtenemos todos los autos desde MongoDB
    context = {
        'car_list': car_list
    }
    return render(request, 'my_first_app/carList.html', context)