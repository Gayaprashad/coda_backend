from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from owner.models import Cars
from datetime import date, datetime
import types
# Create your views here.

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate( username=username, password= password)

        if user is not None:
            auth.login(request,user)
            # messages.success(request, 'You are successfully logged in')
            if user.is_staff ==True:
                return redirect('dashboard')
            else:
                cars=Cars.objects.filter(booked =False)
                context={
                    'cars':cars
                }
                return render(request,'customer.html',context)
        else:
            # messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'index.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('firstentry')

def customer(request):
    cars=Cars.objects.filter(booked =False)
    context={
        'cars':cars
    }
    return render(request,'customer.html',context)

def book(request):
    if request.method == 'POST':
        carId = request.POST['carId']
        fromDate = request.POST['from_date']
        toDate = request.POST['to_date']
        print(carId +" "+fromDate+" "+toDate)
        cars_specific = Cars.objects.filter(id=carId)
        if fromDate< toDate:
            for car in cars_specific:
                car.from_date= fromDate
                car.to_date=toDate
                car.booked = True
                car.userId= request.user.id
                car.save()
        else:
            print("error from date is greater than to date")
        return redirect('customer')

def firstEntry(request):
    today = date.today()
    cars= Cars.objects.all()
    
    
    for car in cars:
        # car_date=  datetime.strptime(str(car.to_date), '%y/%m/%d')
        # print(car.to_date)
        # print(type(car.to_date))
        if car.to_date is not None:
            if car.to_date < today:
                car.from_date= None
                car.to_date=None
                car.userId= None
                car.booked= False
                car.save()
    return render(request,'index.html')

