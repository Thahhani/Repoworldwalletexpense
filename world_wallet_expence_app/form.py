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
        fields=['roomnumber','roomtype','bedtype','price','roomservice','status','roomimage','location']
class roomeditform(ModelForm):
    class Meta:
        model=RoomTable        
        fields=['roomnumber','roomtype','bedtype','price','roomservice','status','roomimage','location']
class rentvehform(ModelForm):
    class Meta:
        model=RentedVehicleTable       
        fields=['location','contactno','vehicletype','rent','description']
class rentveheditform(ModelForm):
    class Meta:
        model=RentedVehicleTable       
        fields=['location','contactno','vehicletype','rent','description']
class spotaddform(ModelForm):
    class Meta:
        model=SpotTable       
        fields=['location','placename','description','ticket','ticket_charge']
class spoteditform(ModelForm):
    class Meta:
        model=SpotTable       
        fields=['location','placename','description','ticket','ticket_charge']
