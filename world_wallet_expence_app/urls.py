from django.contrib import admin
from django.urls import path

from world_wallet_expence_app.views import *


urlpatterns = [
    path('',Login.as_view(),name='Login'),
    path('',Logout.as_view(),name='Logout'),

    #////////////////////admin//////////////////
    path('booking',Booking.as_view(),name='booking'),
    path('complaint/', Complaint.as_view(), name='complaint'),
    path('complaint/reply/<int:reply_id>/', Complaint.as_view(), name='reply_complaint'),
    path('home',Home.as_view(),name='home'),
    path('restaurant',Restaurant.as_view(),name='restaurant'),
    path('acceptrest/<int:r_id>/', Accept_Restaurant.as_view(),name='Accept_Restaurant'),
    path('rejectrest/<int:r_id>/', Reject_Restaurant.as_view(),name='Reject_Restaurant'),
    path('room',Room.as_view(),name='room'),
    path('user',User.as_view(),name='user'),
    path('acceptuser/<int:u_id>/', Accept_User.as_view(),name='Accept_User'),
    path('rejectuser/<int:u_id>/', Reject_User.as_view(),name='Reject_User'),
    path('Deleteroomrev/<int:d_id>/',Deleteroomrev.as_view(),name='Deleteroomrev'),
    path('Rentvehadd',Rentvehadd.as_view(),name='Rentvehadd'),
    path('rentvehedit/<int:e_id>/',rentvehedit.as_view(),name='rentvehedit'),
    path('viewrentveh',viewrentveh.as_view(),name='viewrentveh'), 
    path('Deleterentveh/<int:d_id>/',Deleterentveh.as_view(),name='Deleterentveh'),
    path('spotadd',spotadd.as_view(),name='spotadd'),
    path('spotview',spotview.as_view(),name='spotview'),
    path('spotedit/<int:e_id>/',spotedit.as_view(),name='spotedit'),
    path('Deletespot/<int:d_id>/',Deletespot.as_view(),name='Deletespot'),
    # //////////RESTAURANT///////////////////
    path('Register',Register.as_view(),name='register'),
    path('Add',Add.as_view(),name='Add'),
    path('foodview',Foodview.as_view(),name='foodview'),
    path('foodedit/<int:e_id>/',Foodedit.as_view(),name='foodedit'),
    path('Deletefood/<int:d_id>/',Deletefood.as_view(),name='Deletefood'),
    path('HomeRS',HomeRS.as_view(),name='HomeRS'),
    path('Resreview',Resreview.as_view(),name='Resreview'),
    path('viewfood',Viewfood.as_view(),name='viewfood'),
    path('viewuser',Viewuser.as_view(),name='viewuser'),
    path('restcomplaint',restcomplaint.as_view(),name='restcomplaint'),
    path('restcomplaint/reply/<int:reply_id>/', restcomplaint.as_view(), name='reply_restcomplaint'),
    # ///////////////ROOM////////////////////////
    path('HomeR',HomeR.as_view(),name='HomeR'),
    path('Manage',Manage.as_view(),name='Manage'),
    path('viewRoom',viewRoom.as_view(),name='viewRoom'), 
    path('roomedit/<int:e_id>/',roomedit.as_view(),name='roomedit'),
    path('Deleteroom/<int:d_id>/',Deleteroom.as_view(),name='Deleteroom'),
    path('Review',Review.as_view(),name='Review'),
    path('Send',Send.as_view(),name='Send'),
    path('Send/reply/<int:reply_id>/', Send.as_view(), name='reply_complaint'),
    path('Viewbooking',Viewbooking.as_view(),name='Viewbooking'),
    #////////////API/////////////////////////////
    path('LoginPage',LoginPage.as_view(),name='LoginPage'),
    path('UserReg',UserReg.as_view(),name='UserReg'),
    path('viewrestaurant',viewrestaurant.as_view(),name='viewrestaurant'),
    path('viewfoodorder',viewfoodorder.as_view(),name='viewfoodorder'),
    path('roombooking',roombooking.as_view(),name='roombooking'),
    path('viewroom',viewroom.as_view(),name='viewroom'),
    
    
    path('ViewWalletBalance/<int:l_id>/', ViewWalletBalance.as_view(), name='view_wallet_balance'),
    path('Addwalletbalance/<int:l_id>/',Addwalletbalance.as_view(),name='Addwalletbalance'),
    path('TransactionHistory/<int:l_id>/', TransactionHistory.as_view(), name='transaction_history'),
    path('RoomBookingHistory/<int:l_id>/',RoomBookingHistory.as_view(),name='RoomBookingHistory'),
    path('AddRoom_Rating_Feedback/', AddRoom_Rating_Feedback.as_view(), name='AddRoom_Rating_Feedback'),
    path('AddfoodRating', AddfoodRating.as_view(), name='AddfoodRating'),
    path('Viewnotifications/<int:l_id>/', ViewNotifications.as_view(), name='Viewnotifications'),
    path('food_order_history/<str:loginid>/', FoodOrderHistoryView.as_view(), name='food_order_history'),
    path('cancelBooking/<int:booking_id>/', CancelBooking.as_view(), name='cancel_booking'), 
    path('FoodMenuView/<int:restaurant_id>/', FoodMenuView.as_view(), name='foodmenu'),
    path('place_food_order/', PlaceFoodOrderView.as_view(), name='place_food_order'),
    path('generate-itinerary/', ItineraryView.as_view(), name='generate_itinerary'),
]
  



    

