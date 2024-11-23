from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)
    Type = models.CharField(max_length=20, null=True, blank=True)

class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=20, null=True,blank=True) 
    phone=models.CharField(max_length=20, null=True,blank=True) 
    place=models.CharField(max_length=25, null=True,blank=True) 

class WalletTable(models.Model):
      USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE)
      Balance=models.CharField(max_length=20, null=True,blank=True) 

class TransactionTable(models.Model):
     USERID=models.ForeignKey(WalletTable, on_delete=models.CASCADE)
     amount=models.CharField(max_length=20, null=True,blank=True)
     transactiontype=models.CharField(max_length=20, null=True,blank=True) 
 
class ExpenseTable(models.Model):
     USERID=models.ForeignKey(TransactionTable, on_delete=models.CASCADE)
     BOOKINGID=models.ForeignKey(TransactionTable, on_delete=models.CASCADE)
     ORDERID=models.ForeignKey(TransactionTable, on_delete=models.CASCADE)

class BookingTable(models.Model):
     USERID=models.ForeignKey(ExpenseTable, on_delete=models.CASCADE)      
