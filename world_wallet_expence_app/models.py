from django.db import models


# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)
    Type = models.CharField(max_length=20, null=True, blank=True)
    status=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
         return self.Username


class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=20, null=True,blank=True) 
    phone=models.CharField(max_length=20, null=True,blank=True) 
    place=models.CharField(max_length=25, null=True,blank=True) 
    status=models.CharField(max_length=25, null=True,blank=True) 

class WalletTable(models.Model):
      USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE)
      Balance=models.FloatField(null=True,blank=True) 

class TransactionTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     amount=models.FloatField(null=True,blank=True)
     transactiontype=models.CharField(max_length=20, null=True,blank=True) 
 

class RoomTable(models.Model):
     LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
     roomnumber=models.CharField(max_length=20, null=True,blank=True)
     roomtype=models.CharField(max_length=20, null=True,blank=True)
     bedtype=models.CharField(max_length=20, null=True,blank=True)
     roomimage=models.FileField(upload_to='roomimages/',null=True,blank=True)
     location=models.CharField(max_length=100,null=True,blank=True)
     price=models.CharField(max_length=20, null=True,blank=True) 
     roomservice=models.CharField(max_length=20, null=True,blank=True)
     status=models.CharField(max_length=25, null=True,blank=True) 
     name=models.CharField(max_length=100,null=True,blank=True)
 

class BookingTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)      
     ROOMID=models.ForeignKey(RoomTable, on_delete=models.CASCADE)
     bookingstatus=models.CharField(max_length=20, null=True,blank=True)
     checkindate=models.DateField(null=True,blank=True)
     checkoutdate=models.DateField(null=True,blank=True)
     price=models.CharField(max_length=20, null=True,blank=True)
     paymentmethod=models.CharField(max_length=20, null=True,blank=True)
    

class RestaurantTable(models.Model):
     LOGINID =models.ForeignKey(LoginTable, on_delete=models.CASCADE)
     name=models.CharField(max_length=20, null=True,blank=True)
     place=models.CharField(max_length=20, null=True,blank=True)
     phoneno=models.BigIntegerField(null=True,blank=True)
     email=models.CharField(max_length=20, null=True,blank=True)

# class RoomComplaintTable(models.Model):
#      LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
#      complaint=models.CharField(max_length=20, null=True,blank=True)
#      reply=models.CharField(max_length=20, null=True,blank=True)
#      created_at=models.DateField(auto_now_add=True)

# class RestaurantComplaintTable(models.Model):
#      USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
#      complaint=models.CharField(max_length=20, null=True,blank=True)
#      reply=models.CharField(max_length=20, null=True,blank=True)
#      created_at=models.DateField(auto_now_add=True)

class FoodmenuTable(models.Model):
     RESTAURANTID=models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
     foodname=models.CharField(max_length=20, null=True,blank=True)
     foodtype=models.CharField(max_length=20, null=True,blank=True)
     description=models.CharField(max_length=100, null=True,blank=True)
     price=models.CharField(max_length=20, null=True,blank=True)


class FeedbackTableforRestaurant(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     rating=models.CharField(max_length=20, null=True,blank=True)
     feedback=models.CharField(max_length=20, null=True,blank=True)
     reply=models.CharField(max_length=20, null=True,blank=True)
     MENUID=models.ForeignKey(FoodmenuTable, on_delete=models.CASCADE,null=True,blank=True)
     RESTAURANTID=models.ForeignKey(RestaurantTable, on_delete=models.CASCADE,null=True,blank=True)

class FeedbackTableforRoom(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     rating=models.CharField(max_length=20, null=True,blank=True)
     feedback=models.CharField(max_length=20, null=True,blank=True)
     reply=models.CharField(max_length=20, null=True,blank=True)
     ROOMID=models.ForeignKey(RoomTable, on_delete=models.CASCADE)
     

class OrderitemTable(models.Model):
     
     MENUID=models.ForeignKey(FoodmenuTable, on_delete=models.CASCADE)
     quantity=models.CharField(max_length=20, null=True,blank=True)
     created_at=models.DateField(auto_now_add=True)
     status=models.CharField(max_length=20, null=True,blank=True)

class FoodorderTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE,null=True,blank=True)
     status=models.CharField(max_length=20, null=True,blank=True)
     ORDERID=models.ManyToManyField(OrderitemTable) 
     created_at=models.DateField(auto_now_add=True)



class ExpenseTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     BOOKINGID=models.ForeignKey(BookingTable, on_delete=models.CASCADE)
     ORDERID=models.ForeignKey(OrderitemTable, on_delete=models.CASCADE)





class Notification(models.Model):
   
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name='sent_notifications', null=True, blank=True)
    status=models.CharField(max_length=20, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class RentedVehicleTable(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    contactno = models.CharField(max_length=15, null=True, blank=True)
    vehicletype = models.CharField(max_length=50, null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True) 
    description = models.TextField(null=True, blank=True) # Changed to IntegerField for numeric queries

class SpotTable(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    placename = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ticket = models.CharField(max_length=10, choices=(('free', 'Free'), ('paid', 'Paid')))
    ticket_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For paid spots
 
    
class Chat_History(models.Model):
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    user_query = models.TextField()  # User's query
    chatbot_response = models.TextField()  # Chatbot's response
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the interaction

    def _str_(self):
        return f"Chat at {self.timestamp}"  
# from django.db import models

# class ChatHistory(models.Model):
#     user_query = models.TextField()  # User's query
#     chatbot_response = models.TextField()  # Chatbot's response
#     timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the interaction
#     session_id = models.CharField(max_length=255)  # Add this field to track the session

#     def __str__(self):
#         return f"Chat at {self.timestamp} for session {self.session_id}"





          


 
