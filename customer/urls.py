from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.firstEntry, name='firstentry'),
    path('login',views.login, name='login'),
    path('book', views.book, name='book'),
    path('customer', views.customer, name='customer'),
    path('logout', views.logout, name='logout'),
]