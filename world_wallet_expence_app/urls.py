from django.contrib import admin
from django.urls import path

from world_wallet_expence_app.views import *


urlpatterns = [
    path('Login',Login.as_view(),name='Login'),
    #////////////////////admin//////////////////
    path('booking',Booking.as_view(),name='booking'),
    path('complaint',Complaint.as_view(),name='complaint'),
    path('home',Home.as_view(),name='home'),
    path('restaurant',Restaurant.as_view(),name='restaurant'),
    path('room',Room.as_view(),name='room'),
    path('user',User.as_view(),name='user'),
    # //////////RESTAURANT///////////////////
    path('Regiester',Regiester.as_view(),name='regiester'),
    path('Add',Add.as_view(),name='Add'),
    path('HomeRS',HomeRS.as_view(),name='HomeRS'),
    path('Resreview',Resreview.as_view(),name='Resreview'),
    path('viewfood',Viewfood.as_view(),name='viewfood'),
    path('viewuser',Viewuser.as_view(),name='viewuser'),
    # ///////////////ROOM////////////////////////
    path('HomeR',HomeR.as_view(),name='HomeR'),
    path('Manage',Manage.as_view(),name='Manage'),
    path('Review',Review.as_view(),name='Review'),
    path('Send',Send.as_view(),name='Send'),
    path('Viewbooking',Viewbooking.as_view(),name='Viewbooking'),

    
]
