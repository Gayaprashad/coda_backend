from django.urls import path
from . import views

urlpatterns=[
    path('', views.apiOverview, name="api-overview"),
    path('cars-list', views.carsList, name="cars-list"),
    path('cars-update/<str:pk>', views.carsUpdate, name="cars-update"),
    path('dashboard', views.dashboardList, name="dashboard"),
]