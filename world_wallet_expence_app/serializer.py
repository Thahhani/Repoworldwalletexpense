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
