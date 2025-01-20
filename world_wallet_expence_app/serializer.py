from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

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
        fields=['name','place','phoneno','email','id']
class FoodorderSerializer(ModelSerializer):
    class Meta:
        model=OrderitemTable
        fields=['quantity','created_at',' status']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTable
        fields = ['USERID', 'Balance'] 


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTable
        fields = ['USERID', 'amount', 'transactiontype']


class RoomSerializer(ModelSerializer):
    class Meta:
        model=RoomTable
        fields=['id','roomnumber','roomtype','bedtype','price','roomservice','status', 'location', 'roomimage','name']

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['USERID', 'ROOMID', 'bookingstatus', 'checkindate', 'checkoutdate', 'price','paymentmethod']

class Rating_FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTableforRoom
        fields = ['USERID', 'ROOMID', 'rating', 'feedback',]

class FoodRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTableforRestaurant
        fields = ['USERID', 'RESTAURANTID', 'MENUID', 'rating', 'feedback',]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'sender', 'status','created_at']

class FoodmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodmenuTable
        fields = ['id', 'RESTAURANTID', 'foodname', 'foodtype', 'description', 'price']

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['Name', 'phone', 'place', 'status']
class OrderItemSerializer(serializers.ModelSerializer):
    MENUID = FoodmenuSerializer()  # Nested serializer to fetch the foodname

    class Meta:
        model = OrderitemTable
        fields = ['MENUID', 'quantity', 'created_at', 'status']

# Main serializer for the FoodorderTable
class FoodOrderSerializer(serializers.ModelSerializer):
    ORDERID = OrderItemSerializer()  # Nested serializer to include order details and foodname

    class Meta:
        model = FoodorderTable
    
        fields = ['USERID', 'status', 'ORDERID', 'created_at']
class OrderItemSerializer1(serializers.ModelSerializer):
    MENUID = serializers.StringRelatedField()  # Assuming FoodmenuTable has a meaningful __str__ method

    class Meta:
        model = OrderitemTable
        fields = ['MENUID', 'quantity', 'created_at', 'status']

class FoodOrderSerializer1(serializers.ModelSerializer):
    ORDERID = OrderItemSerializer(many=True)  # Correctly handle the ManyToMany relationship

    class Meta:
        model = FoodorderTable
        fields = ['USERID', 'status', 'ORDERID', 'created_at']

class RoomTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTable
        fields = '__all__'

class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = '__all__'

class RentedVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedVehicleTable
        fields = '__all__'

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotTable
        fields = '__all__'

