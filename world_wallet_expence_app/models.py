from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)
    Type = models.CharField(max_length=20, null=True, blank=True)
    status=models.CharField(max_length=20, null=True, blank=True)


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
     price=models.CharField(max_length=20, null=True,blank=True) 
     roomservice=models.CharField(max_length=20, null=True,blank=True)
     status=models.CharField(max_length=25, null=True,blank=True) 
 

class BookingTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)      
     ROOMID=models.ForeignKey(RoomTable, on_delete=models.CASCADE)
     bookingstatus=models.CharField(max_length=20, null=True,blank=True)
     checkindate=models.DateField(null=True,blank=True)
     checkoutdate=models.DateField(null=True,blank=True)
     paymentmethod=models.CharField(max_length=20, null=True,blank=True)
    

class RestaurantTable(models.Model):
     LOGINID =models.ForeignKey(LoginTable, on_delete=models.CASCADE)
     name=models.CharField(max_length=20, null=True,blank=True)
     place=models.CharField(max_length=20, null=True,blank=True)
     phoneno=models.BigIntegerField(null=True,blank=True)
     email=models.CharField(max_length=20, null=True,blank=True)

class RoomComplaintTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     complaint=models.CharField(max_length=20, null=True,blank=True)
     reply=models.CharField(max_length=20, null=True,blank=True)
     created_at=models.DateField(auto_now_add=True)

class RestaurantComplaintTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     complaint=models.CharField(max_length=20, null=True,blank=True)
     reply=models.CharField(max_length=20, null=True,blank=True)
     created_at=models.DateField(auto_now_add=True)


class FeedbackTableforRestaurant(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     rating=models.CharField(max_length=20, null=True,blank=True)
     feedback=models.CharField(max_length=20, null=True,blank=True)
     RESTAURANTID=models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)

class FeedbackTableforRoom(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     rating=models.CharField(max_length=20, null=True,blank=True)
     feedback=models.CharField(max_length=20, null=True,blank=True)
     ROOMID=models.ForeignKey(RoomTable, on_delete=models.CASCADE)

class FoodmenuTable(models.Model):
     RESTAURANTID=models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
     foodname=models.CharField(max_length=20, null=True,blank=True)
     foodtype=models.CharField(max_length=20, null=True,blank=True)
     description=models.CharField(max_length=100, null=True,blank=True)
     price=models.CharField(max_length=20, null=True,blank=True)

class FoodorderTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     status=models.CharField(max_length=20, null=True,blank=True)
     created_at=models.DateField(auto_now_add=True)

class OrderitemTable(models.Model):
     ORDERID=models.ForeignKey(FoodorderTable, on_delete=models.CASCADE)
     MENUID=models.ForeignKey(FoodmenuTable, on_delete=models.CASCADE)
     quantity=models.CharField(max_length=20, null=True,blank=True)
     created_at=models.DateField(auto_now_add=True)
     status=models.CharField(max_length=20, null=True,blank=True)

class ExpenseTable(models.Model):
     USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
     BOOKINGID=models.ForeignKey(BookingTable, on_delete=models.CASCADE)
     ORDERID=models.ForeignKey(OrderitemTable, on_delete=models.CASCADE)