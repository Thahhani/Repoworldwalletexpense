from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['Name','phone','place','status']
class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','Type','status']
class RestaurantSerializer(ModelSerializer):
    class Meta:
        model=RestaurantTable
        fields=['name','place','phoneno','email']
class FoodorderSerializer(ModelSerializer):
    class Meta:
        model=OrderitemTable
        fields=['quantity','created_at',' status']
class WalletSerializer(ModelSerializer):
    class Meta:
        model=WalletTable
        fields=['Balance']
class RoomSerializer(ModelSerializer):
    class Meta:
        model=RoomTable
        fields=['roomnumber','roomtype','bedtype','price','roomservice','status']
class BookingSerializer(ModelSerializer):
    class Meta:
        model=BookingTable
        fields=['bookingstatus','checkindate','checkoutdate','paymentmethod']
