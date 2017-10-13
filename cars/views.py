from django.shortcuts import render

# Create your views here.
def cars(request):
    return render("cars/cars.html")
