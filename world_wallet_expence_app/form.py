from django.forms import ModelForm
from .models import *

# class addroomform(ModelForm):
#     class Meta:
#         model=RoomTable
#         fields=['roomnumber','type','price','status']


class replyform(ModelForm):
    class Meta:
        model=RoomComplaintTable
        fields=['reply']
class reply1form(ModelForm):
    class Meta:
        model=RestaurantComplaintTable
        fields=['reply']

class foodaddform(ModelForm):
    class Meta:
        model=FoodmenuTable        
        fields=['foodname','foodtype','price','description']

class foodeditform(ModelForm):
    class Meta:
        model=FoodmenuTable        
        fields=['foodname','foodtype','price','description']
class manageform(ModelForm):
    class Meta:
        model=RoomTable        
        fields=['roomnumber','roomtype','bedtype','price','roomservice','status']
class roomeditform(ModelForm):
    class Meta:
        model=RoomTable        
        fields=['roomnumber','roomtype','bedtype','price','roomservice','status']
