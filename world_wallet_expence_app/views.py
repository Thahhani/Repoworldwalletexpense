from django.shortcuts import render
from django.views import View

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html")
    
    # //////////////////////////////////// ADMIN /////////////////////////////////////////////////////////

class Booking(View):
    def get(self,request):
        return render(request,"ADMIN/booking.html")
class Complaint(View):
    def get(self,request):
        return render(request,"ADMIN/complaint.html")
class Home(View):
    def get(self,request):
        return render(request,"ADMIN/home.html")
class Restaurant(View):
    def get(self,request):
        return render(request,"ADMIN/restaurant.html")
class Room(View):
    def get(self,request):
        return render(request,"ADMIN/room.html")
class User(View):
    def get(self,request):
        return render(request,"ADMIN/user.html")
# ///////////////////////////////// RESTAURANT //////////////////////////////////////////////////////////////
class Regiester(View):
    def get(self,request):
        return render(request,"regiester.html")
class Add(View):
    def get(self,request):
        return render(request,"RESTAURANT/add.html")
class HomeRS(View):
    def get(self,request):
        return render(request,"RESTAURANT/homeRS.html")
class Resreview(View):
    def get(self,request):
        return render(request,"RESTAURANT/resreview.html")
class Viewfood(View):
    def get(self,request):
        return render(request,"RESTAURANT/viewfood.html")
class Viewuser(View):
    def get(self,request):
        return render(request,"RESTAURANT/viewuser.html")
# //////////////////ROOM////////////////////////////////////
class HomeR(View):
    def get(self,request):
        return render(request,"ROOM/homeR.html")
class Manage(View):
    def get(self,request):
        return render(request,"ROOM/manage.html")
class Review(View):
    def get(self,request):
        return render(request,"ROOM/review.html")
class Send(View):
    def get(self,request):
        return render(request,"ROOM/send.html")
class Viewbooking(View):
    def get(self,request):
        return render(request,"ROOM/viewbooking.html")


