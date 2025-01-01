from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages

from world_wallet_expence_app.form import *

from .models import *
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework import status
from rest_framework.response import Response
from .serializer import *



# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        username = request.POST.get('username')  # Use .get() to avoid KeyError if key is missing
        password = request.POST.get('password')

        try:
            # Attempt to find the user by username and password
            login_obj = LoginTable.objects.get(Username=username, Password=password)
            
            # Set session variable if login is successful
            request.session["loginid"] = login_obj.id
            print(request.session["loginid"])

            # Fetch the restaurant ID if the user type is "restaurant"
            if login_obj.Type == "restaurant":
                # Fetch the related RestaurantTable object
                restaurant = RestaurantTable.objects.get(LOGINID=login_obj.id)
                print(restaurant.id)
                request.session["restaurant_id"] = restaurant.id  # Store restaurant ID in session
                
                return HttpResponse('''<script>alert("Welcome to home");window.location="/HomeRS"</script>''')
            if login_obj.Type == "admin":
                # Fetch the related RestaurantTable object
               
                
                 # Store restaurant ID in session
                
                return HttpResponse('''<script>alert("Welcome to home");window.location="/home"</script>''')
            elif login_obj.Type == "room":
              print("mmmm",login_obj)
              room = RoomTable.objects.filter(LOGINID=login_obj).first()  # Get the first match or None
              if room:
                print("rrrrrr",room.id)
                request.session["room_id"] = room.id
                return HttpResponse('''<script>alert("Welcome to home");window.location="/HomeR"</script>''')
            else:
              return HttpResponse('Room not found', status=404)



            # Handle user redirection based on the Type (role)
            if login_obj.Type == "admin":
                return HttpResponse('''<script>alert("Welcome to home");window.location="/home"</script>''')
            elif login_obj.Type == "room":
                return HttpResponse('''<script>alert("Welcome to home");window.location="/HomeR"</script>''')

        except LoginTable.DoesNotExist:
            # If no matching user is found
            return HttpResponse('''<script>alert("Invalid credentials. Please try again.");window.location="/login"</script>''')

class Logout(View):
    def get(self, request):
        return render(request, "login.html")
        








    
    
    # //////////////////////////////////// ADMIN /////////////////////////////////////////////////////////
class Home(View):
    def get(self,request):
        return render(request,"ADMIN/home.html")
class Restaurant(View):
    def get(self,request):
        obj=RestaurantTable.objects.filter(LOGINID__status='pending')
        return render(request,"ADMIN/restaurant.html",{'val':obj})
class Accept_Restaurant(View):
    def get(self,request,r_id):
        rest=RestaurantTable.objects.get(id=r_id)
        rest.LOGINID.Type='restaurant'
        rest.LOGINID.save()
        return HttpResponse('''<script>alert("ACCEPTED");window.location="/restaurant"</script>''')

class Reject_Restaurant(View):
    def get(self,request,r_id):
        print("gggg")
        rest=RestaurantTable.objects.get(id=r_id)
        rest.LOGINID.Type='Rejected'
        rest.LOGINID.save()
        return HttpResponse('''<script>alert("Rejected");window.location="/restaurant"</script>''')

class Booking(View):
    def get(self,request):
        r=BookingTable.objects.all()
        return render(request,"ADMIN/booking.html",{'r':r})
        
class Complaint(View):
    def get(self, request):
        u=RoomComplaintTable.objects.filter(LOGINID__Type='room')
        f = RestaurantComplaintTable.objects.all()
        return render(request, "ADMIN/complaint.html", {'f': f,'u':u})
    
    def post(self, request, reply_id):
        complaint = get_object_or_404(RoomComplaintTable,RestaurantComplaintTable, id=reply_id)
        form = replyform(request.POST, instance=complaint)
        
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Replied");window.location="/complaint"</script>''')
        return HttpResponse('''<script>alert("Error occurred while replying");window.location="/complaint"</script>''')


class Room(View):
    def get(self,request):
        r=RoomTable.objects.all()
        return render(request,"ADMIN/room.html",{'r':r})


class User(View):
    def get(self,request):
        u=UserTable.objects.filter(LOGINID__status='pending')
        print(u)
        return render(request,"ADMIN/user.html",{'u':u})
class Accept_User(View):
    def get(self,request,u_id):
        print("gggg")
        user=UserTable.objects.get(id=u_id)
        print(user)
        user.LOGINID.Type='user'
        user.LOGINID.save()
        return HttpResponse('''<script>alert("ACCEPTED");window.location="/user"</script>''')
class Reject_User(View):
    def get(self,request,u_id):
        print("gggg")
        rest=UserTable.objects.get(id=u_id)
        rest.LOGINID.Type='rejected'
        rest.LOGINID.save()
        return HttpResponse('''<script>alert("REJECTED");window.location="/user"</script>''')
    

    


# ///////////////////////////////// RESTAURANT //////////////////////////////////////////////////////////////
class Register(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
         type = request.POST['type']
         name = request.POST['name']
         Place = request.POST['Place']
         Email = request.POST['Email']
         Phone = request.POST['Phone']
         username = request.POST['UserName']
         Password = request.POST['Password']
         if type == '1':
            login_obj = LoginTable()
            login_obj.Username = username
            login_obj.Password = Password
            login_obj.Type = 'Room'
            login_obj.status = "pending"

            login_obj.save()
            obj = RestaurantTable()
            obj.name=name
            obj.place=Place
            obj.phoneno=Phone
            obj.email=Email
            obj.LOGINID=login_obj
            obj.save()
            return HttpResponse('''<script>alert("Hotel successfully register");window.location="/"</script>''')
         elif type =='2':
            login_obj = LoginTable()
            login_obj.Username = username
            login_obj.Password = Password
            login_obj.Type = 'Restaurant'
            login_obj.status = "pending"

            login_obj.save()
            obj = RestaurantTable()
            obj.name=name
            obj.place=Place
            obj.phoneno=Phone
            obj.email=Email
            obj.LOGINID=login_obj
            obj.save()
            return HttpResponse('''<script>alert("Restaurant successfully register");window.location="/"</script>''')
         
class Deleteroomrev(View):
    def get(self,request,d_id):
        obj=RoomTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("room successfully deleted");window.location="/room"</script>''')

         
class Add(View):
    def get(self,request):
        return render(request,"RESTAURANT/add.html")
    def post(self,request):
        form=foodaddform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            print("%%%%%%%%%%", request.session["loginid"])
            f.RESTAURANTID=RestaurantTable.objects.get(LOGINID_id=request.session["loginid"])
            f.save()
            return HttpResponse('''<script>alert("item is added");window.location="/foodview"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/Add"</script>''')
    

            
class Foodview(View):
    def get(self,request):
        obj=FoodmenuTable.objects.all()
        return render(request,"RESTAURANT/foodview.html",{'val':obj})
class Foodedit(View):
    def get(self,request,e_id):
        obj = FoodmenuTable.objects.get(id=e_id)
        return render(request,"RESTAURANT/foodedit.html",{'val':obj})
    def post(self,request,e_id):
        obj=FoodmenuTable.objects.get(id=e_id)
        print(obj)
        form=foodeditform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is added");window.location="/foodview"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/foodedit"</script>''')
class Deletefood(View):
    def get(self,request,d_id):
        obj=FoodmenuTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("successfully deleted");window.location="/foodview"</script>''')
    
class HomeRS(View):
    def get(self,request):
        return render(request,"RESTAURANT/homeRS.html")
class Resreview(View):
    def get(self,request):
          restaurant_id = request.session.get("restaurant_id")

          r = FeedbackTableforRestaurant.objects.filter(RESTAURANTID=restaurant_id)
          return render(request,"RESTAURANT/resreview.html",{'r':r})
    
class Viewfood(View):
    def get(self,request):
        v = OrderitemTable.objects.all()
        return render(request,"RESTAURANT/viewfood.html",{'v':v})
class Viewuser(View):
    def get(self,request):
         u = UserTable.objects.all()
         return render(request,"RESTAURANT/viewuser.html",{'u':u})
class restcomplaint(View):
    def get(self,request):
        u = RestaurantComplaintTable.objects.all()
        return render(request,"RESTAURANT/restcomplaint.html",{'u':u})
    def post(self, request, reply_id):
        complaint = get_object_or_404(RestaurantComplaintTable, id=reply_id)
        form = reply1form(request.POST, instance=complaint)
        
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Replied");window.location="/restcomplaint"</script>''')
        return HttpResponse('''<script>alert("Error occurred while replying");window.location="/restcomplaint"</script>''')
# //////////////////ROOM////////////////////////////////////
class HomeR(View):
    def get(self,request):
        return render(request,"ROOM/homeR.html")
class Manage(View):
    def get(self, request):
        # Renders the form for GET requests
        return render(request, "ROOM/manage.html")

    def post(self, request):
        print("Entering POST function...")  # Debugging line
        
        # Handle POST request to add new data
        form = manageform(request.POST)

        if form.is_valid():
            print("Form is valid!") 
            id = request.session.get("loginid")
            print(id)
            if not id:
                messages.error(request, "User not logged in.")
                return redirect("/Manage")  
            else:
                login_instance = LoginTable.objects.get(id=id)
                f = form.save(commit=False)
                f.LOGINID = login_instance  # Assign the LoginTable instance, not just the id
                f.save()
                return HttpResponse('''<script>alert("item is added");window.location="/viewroom"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/Manage"</script>''')


                  

class viewroom(View):
    def get(self,request):
         obj=RoomTable.objects.all()
         return render(request,"ROOM/viewroom.html",{'val':obj})
class roomedit(View):
    def get(self,request,e_id):
        obj = RoomTable.objects.get(id=e_id)
        return render(request,"ROOM/roomedit.html",{'val':obj})
    def post(self,request,e_id):
        obj=RoomTable.objects.get(id=e_id)
        print(obj)
        form=roomeditform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is update");window.location="/viewroom"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/roomedit"</script>''')
class Deleteroom(View):
    def get(self,request,d_id):
        obj=RoomTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("successfully deleted");window.location="/viewroom"</script>''')
# class Review(View):
#     def get(self,request):
#         room_id = request.session.get("room_id")

#         r = FeedbackTableforRoom.objects.filter(ROOMID=room_id)
#         print(r)
#         return render(request,"ROOM/review.html",{'r':r})
class Review(View):
    def get(self, request):
        room_id = request.session.get("room_id")
        if not room_id:
            return HttpResponse('Room ID not found in session', status=404)

        r = FeedbackTableforRoom.objects.filter(ROOMID=room_id)
        print(r)
        return render(request, "ROOM/review.html", {'r': r})

class Send(View):
    def get(self,request):
        u = RoomComplaintTable.objects.all()
        return render(request,"ROOM/send.html",{'u':u})
    def post(self, request, reply_id):
        complaint = get_object_or_404(RoomComplaintTable, id=reply_id)
        form = replyform(request.POST, instance=complaint)
        
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Replied");window.location="/Send"</script>''')
        return HttpResponse('''<script>alert("Error occurred while replying");window.location="/Send"</script>''')
class Viewbooking(View):
    def get(self,request):
        obj=BookingTable.objects.all()
        return render(request,"ROOM/viewbooking.html",{'val':obj})

    # ///////////////////////////////////////// API ////////////////////////////////////////////////////////


class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(Username=username,Password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Check password using check_password
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict, status=HTTP_200_OK)
    
class UserReg(APIView):
    def post(self,requset):
        print(request.data)
        user_serial = UserSerializer(data=request.data)
        Login_serial =LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = Login_serial.is_valid()

        if data_valid and login_valid:
            password = request.data['password']
            login_profile = Login_serial.save(user_type='USER', password=password)
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': Login_serial.errors if not login_valid else None,
                         'user_error': user_serial.error if not data_valid else None},status=status.HTTP_400_BAD_REQUEST)
class viewrestaurant(APIView):
    def get(self,request):
        restaurant = RestaurantTable.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurant,many = True)
        print(restaurant_serializer)
        return Response(restaurant_serializer.data)
class viewfoodorder(APIView):
    def get(self,request):
        foodorder = OrderitemTable.objects.all()
        foodorder_serializer = FoodorderSerializer(foodorder,many = True)
        print(foodorder_serializer)
        return Response(foodorder_serializer.data)
class viewwallet(APIView):
    def get(self,request):
        wallet = WalletTable.objects.all()
        wallet_serializer = WalletSerializer(wallet,many = True)
        print(wallet_serializer)
        return Response(wallet_serializer.data)
class viewroom(APIView):
    def get(self,request):
        room = RoomTable.objects.all()
        room_serializer = RoomSerializer(room,many = True)
        print(room_serializer)
        return Response(room_serializer.data)
class viewbooking(APIView):
    def get(self,request):
        booking = BookingTable.objects.all()
        booking_serializer = BookingSerializer(booking,many = True)
        print(booking_serializer)
        return Response(booking_serializer.data)




