from django.shortcuts import render
from .models import Cars
# Create your views here.

def dashboard(request):
    cars = Cars.objects.all()
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

    context={
        'onRoad': onroad,
        'available': available,
        'mostInDemandLoc': mostInDemandLoc,
        'mostInDemandMod': mostInDemandMod,
    }
    return render(request,'admin.html',context)
    