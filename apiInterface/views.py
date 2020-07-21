from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarsSerializers,DashboardSerializers
from owner.models import Cars
from .models import dashboardData
from datetime import date, datetime
import types

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    # return JsonResponse("ApI BASE POINT", safe=False)
    api_urls= {
        'Book': '/book',
    }
    return Response(api_urls)

@api_view(['GET'])
def carsList(request):
    # Resets the cars which have passed the to_date in the booking 
    today = date.today()
    cars= Cars.objects.all()  
    for car in cars:
        if car.to_date is not None:
            if car.to_date < today:
                car.from_date= None
                car.to_date=None
                car.userId= None
                car.booked= False
                car.save()
    # cars =Cars.objects.all()
    serializer =CarsSerializers(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def carsUpdate(request, pk):
    car = Cars.objects.get(id=pk)
    serializer= CarsSerializers(instance=car, data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def dashboardList(request):
    # Resets the cars which have passed the to_date in the booking 
    today = date.today()
    cars= Cars.objects.all()  
    for car in cars:
        if car.to_date is not None:
            if car.to_date < today:
                car.from_date= None
                car.to_date=None
                car.userId= None
                car.booked= False
                car.save()
    # cars = Cars.objects.all()
    cars_booked = Cars.objects.filter(booked=True)
    onroad =0
    available =0
    for car in cars:
        if car.booked == True:
            onroad+=1
        else:
            available +=1
    print("onroad: "+str(onroad)) 
    print("availabe: "+str(available)) 
    # For finding the location with the hightest number of cars 
    car_loc =Cars.objects.filter(booked=True).order_by('location').distinct('location')
    # car_loc =Cars.objects.filter(booked=True).distinct('location')
    print(car_loc)
    locations=[]
    for car in car_loc:
        locations.append(car.location)
    carsInLoc =[]
    z=0
    for location in locations:
        print(location)
        carsInLoc.append(0)
        for car in cars_booked:
            if car.location== location:
                carsInLoc[z]+=1
        z+=1


    print(locations)
    print(carsInLoc)
    mostInDemandLoc =locations[0]
    mostInDemandLocNo=carsInLoc[0]
    for i in range(1, len(carsInLoc)):
        if int(carsInLoc[i])>mostInDemandLocNo:
            mostInDemandLoc =locations[i]
    
    print("Most in demand Location: "+mostInDemandLoc)

    # For finding the model with the highest number of rentals 
    car_model =Cars.objects.filter(booked=True).order_by('model').distinct('model')
    models=[]
    for car in car_model:
        models.append(car.model)
    carsInMod =[]
    z=0
    for Model in models:
        print(Model)
        carsInMod.append(0)
        for car in cars_booked:
            if car.model== Model:
                carsInMod[z]+=1
        z+=1

    print(models)
    print(carsInMod)
    mostInDemandMod =models[0]
    mostInDemandModNo=carsInMod[0]
    for i in range(1, len(carsInMod)):
        if int(carsInMod[i])>mostInDemandModNo:
            mostInDemandMod =models[i]  
    
    print("Most in demand Model: "+mostInDemandMod)
    dashboardData.objects.all().delete()
    dash = dashboardData(onroad=onroad, available= available, mostInDemandLoc=mostInDemandLoc, mostInDemandMod=mostInDemandMod)
    dash.save()
    serializer = DashboardSerializers(dash, many=False)
    return Response(serializer.data)


