from datetime import timezone
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

import google.generativeai as genai
# import openai






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
    
class Rentvehadd(View):
    def get(self,request,):
         return render(request, "ADMIN/rentvehadd.html")
    
    def post(self, request):
        print("Entering POST function...")  # Debugging line
        
        # Handle POST request to add new data
        form = rentvehform(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is added");window.location="/viewrentveh"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/Rentvehadd"</script>''')
class rentvehedit(View):
    def get(self,request,e_id):
        obj = RentedVehicleTable.objects.get(id=e_id)
        return render(request,"ADMIN/editrentveh.html",{'val':obj})
    def post(self,request,e_id):
        obj=RentedVehicleTable.objects.get(id=e_id)
        print(obj)
        form=rentveheditform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is update");window.location="/viewrentveh"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/rentvehedit"</script>''')
class viewrentveh(View):
    def get(self,request):
         obj=RentedVehicleTable.objects.all()
         return render(request,"ADMIN/viewrentveh.html",{'val':obj})
class Deleterentveh(View):
    def get(self,request,d_id):
        obj=RentedVehicleTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("successfully deleted");window.location="/viewrentveh"</script>''')

class spotadd(View):
    def get(self,request,):
         return render(request,"ADMIN/spotadd.html")
    
    def post(self, request):
        print("Entering POST function...")  # Debugging line
        
        # Handle POST request to add new data
        form = spotaddform(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is added");window.location="/spotview"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/spotadd"</script>''')        

class spotview(View):
    def get(self,request):
         obj=SpotTable.objects.all()
         return render(request,"ADMIN/spotview.html",{'val':obj})  

class spotedit(View):
    def get(self,request,e_id):
        obj = SpotTable.objects.get(id=e_id)
        return render(request,"ADMIN/spotedit.html",{'val':obj})
    def post(self,request,e_id):
        obj=SpotTable.objects.get(id=e_id)
        print(obj)
        form=spoteditform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("item is update");window.location="/spotview"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/spotedit"</script>''')  
    
class Deletespot(View):
    def get(self,request,d_id):
        obj=SpotTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("successfully deleted");window.location="/spotview"</script>''')


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
                return HttpResponse('''<script>alert("item is added");window.location="/viewRoom"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/Manage"</script>''')


                  

class viewRoom(View):
    def get(self,request):
         obj=RoomTable.objects.all()
         return render(request,"ROOM/viewRoom.html",{'val':obj})
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
            return HttpResponse('''<script>alert("item is update");window.location="/viewRoom"</script>''')
        return HttpResponse('''<script>alert("item failed");window.location="/roomedit"</script>''')
class Deleteroom(View):
    def get(self,request,d_id):
        obj=RoomTable.objects.filter(id=d_id)
        print(obj)
        obj.delete()
       
        return HttpResponse('''<script>alert("successfully deleted");window.location="/viewRoom"</script>''')
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
        username = request.data.get("Username")
        password = request.data.get("Password")

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
    def post(self,request):
        user_serial = UserSerializer(data=request.data)
        Login_serial =LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = Login_serial.is_valid()

        if data_valid and login_valid:
            password = request.data['password']
            login_profile = Login_serial.save(Type='USER', Password=password)
            user_serial.save(LOGINID=login_profile)
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
    
# class roombooking(APIView):
#     def post(self,request):
#         print("fffffffffffffffffffffffffffffff",request.data)
#         user_id = request.data.get('USERID')
#         room_id = request.data.get('ROOMID')
#         checkindate = request.data.get('checkindate')
#         checkoutdate = request.data.get('checkoutdate')
#         print("^^^^^^^^^^^^^^^^^^^^^", user_id)
#         user_obj = UserTable.objects.get(LOGINID_id=user_id)
#         room_obj = RoomTable.objects.get(id=room_id)
#         booking_obj=BookingTable()
#         booking_obj.checkindate=checkindate
#         booking_obj.checkoutdate=checkoutdate
#         booking_obj.USERID=user_obj
#         booking_obj.ROOMID=room_obj
#         booking_obj.save()
#         print("saveeeeeeed")
            
#         return Response(status=status.HTTP_201_CREATED)
from datetime import timezone
import datetime     

class roombooking(APIView):
    def post(self, request):
        print("Request Data:", request.data)
        
        # Extracting the necessary data from the request
        user_id = request.data.get('USERID')
        room_id = request.data.get('ROOMID')
        checkindate = request.data.get('checkindate')
        checkoutdate = request.data.get('checkoutdate')
        
        # Fetching the user and room objects
        try:
            user_obj = UserTable.objects.get(LOGINID=user_id)
            room_obj = RoomTable.objects.get(id=room_id)
        except UserTable.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        except RoomTable.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)

        # Creating a new booking
        booking_obj = BookingTable()
        booking_obj.checkindate = checkindate
        booking_obj.checkoutdate = checkoutdate
        booking_obj.USERID = user_obj
        booking_obj.ROOMID = room_obj
        booking_obj.bookingstatus='booked'
        booking_obj.save()

      # Example of fetching an admin
     
        sender_obj = None  # If no admin is available, we'll leave it as None.

        # Creating a notification record
        notification_obj = Notification(
            user=user_obj,
            sender=sender_obj,
            status=f"Booking confirmed for room {room_obj.id} from {checkindate} to {checkoutdate}",
            created_at=datetime.datetime.now(timezone.utc)
        )
        notification_obj.save()

        # Return a success response
        return Response({"message": "Booking and notification created successfully."}, status=status.HTTP_201_CREATED)




    
class ViewWalletBalance(APIView):
    def get(self, request, l_id):
        # Find the user by login_id (l_id in your case)
        user = get_object_or_404(UserTable, LOGINID=l_id)
        print(user)  # Assuming login_id is unique
        
        # Get the wallet for that user
        wallet = get_object_or_404(WalletTable, USERID=user)
        print(wallet)
        
        # Serialize the wallet data
        wallet_serializer = WalletSerializer(wallet)
        
        # Return the serialized data in the response
        return Response(wallet_serializer.data)
    


class Addwalletbalance(APIView):
    def post(self, request, l_id):
        # Add or update the wallet balance for the specific user (POST request)
        user = get_object_or_404(UserTable, LOGINID=l_id)  # Assuming 'login_id' is unique

        # Retrieve the amount to add or set in the wallet from the request data
        balance_to_add = request.data.get("balance", None)
        
        if balance_to_add is None:
            return Response({"error": "Balance amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure that the balance_to_add is converted to float
        try:
            balance_to_add = float(balance_to_add)
        except ValueError:
            return Response({"error": "Invalid balance amount, must be a number"}, status=status.HTTP_400_BAD_REQUEST)

        # Try to get the existing wallet or create a new one if not found
        wallet, created = WalletTable.objects.get_or_create(USERID=user)

        if created:
            # New wallet created, set the initial balance
            wallet.Balance = balance_to_add
        else:
            # If wallet already exists and balance is None, set it to 0.0 before adding the new balance
            if wallet.Balance is None:
                wallet.Balance = 0.0
            wallet.Balance += balance_to_add  # Add the balance if updating

        wallet.save()

        # Serialize and return the updated wallet data
        wallet_serializer = WalletSerializer(wallet)
        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

    


class TransactionHistory(APIView):
    def get(self, request, l_id):
        # Get the user by login_id (l_id)
        user = get_object_or_404(UserTable, LOGINID=l_id)

        # Retrieve all transactions for the given user
        transactions = TransactionTable.objects.filter(USERID=user)

        # Serialize the transaction data
        transaction_serializer = TransactionSerializer(transactions, many=True)

        # Return the serialized data
        return Response(transaction_serializer.data)
    
    
class viewroom(APIView):
    def get(self,request):
        room = RoomTable.objects.all()
        room_serializer = RoomSerializer(room,many = True)
        print(room_serializer)
        return Response(room_serializer.data)
    
class RoomBookingHistory(APIView):
    def get(self, request, l_id):
        # Retrieve the user from UserTable using their login_id (l_id)
        user = get_object_or_404(UserTable, LOGINID=l_id)

        # Fetch all the bookings for this user
        bookings = BookingTable.objects.filter(USERID=user)
        print(bookings)

        # Serialize the bookings data
        booking_serializer = RoomBookingSerializer(bookings, many=True)

        # Return the serialized data as the response
        return Response(booking_serializer.data)
    

class AddRoom_Rating_Feedback(APIView):
    def post(self, request):
        # Extract the data from the request
        l_id = request.data.get("login_id")
        room_id = request.data.get("room_id")
        rating = request.data.get("rating")
        feedback = request.data.get("feedback")

        if not l_id or not room_id or not rating or not feedback:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the user and room by their IDs
        user = get_object_or_404(UserTable, LOGINID=l_id)
        room = get_object_or_404(RoomTable, id=room_id)

        # Create the feedback entry
        feedback_entry = FeedbackTableforRoom.objects.create(
            USERID=user,
            ROOMID=room,
            rating=rating,
            feedback=feedback
        )

        # Serialize the newly created feedback entry
        feedback_serializer = Rating_FeedbackSerializer(feedback_entry)

        # Return the serialized data as the response
        return Response(feedback_serializer.data, status=status.HTTP_201_CREATED)
    

class AddfoodRating(APIView):
    def post(self, request):
        # Extract data from the request body
        l_id = request.data.get("login_id")
        menu_id = request.data.get("menu_id")
        restaurant_id = request.data.get("restaurant_id")
        rating = request.data.get("rating")
        feedback = request.data.get("feedback")

        # Validate that all required fields are present
        if not l_id or not menu_id or not restaurant_id or not rating or not feedback:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the User, Menu, and Restaurant objects
        user = get_object_or_404(UserTable, login_id=l_id)
        menu_item = get_object_or_404(FoodmenuTable, id=menu_id)
        restaurant = get_object_or_404(RestaurantTable, id=restaurant_id)

        # Create the feedback entry in the FeedbackTableforRestaurant model
        feedback_entry = FeedbackTableforRestaurant.objects.create(
            USERID=user,
            MENUID=menu_item,
            RESTAURANTID=restaurant,
            rating=rating,
            feedback=feedback
        )

        # Serialize the feedback entry
        feedback_serializer = FoodRatingSerializer(feedback_entry)

        # Return the serialized feedback data as the response
        return Response(feedback_serializer.data, status=status.HTTP_201_CREATED)
    
class ViewNotifications(APIView):
    """
    View notifications for a user based on their user ID.
    """
    def get(self, request, l_id):
        user = get_object_or_404(UserTable, LOGINID=l_id)

        notifications = Notification.objects.filter(user=user)
        print(notifications)

        # Serialize the notifications
        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodOrderHistoryView(APIView):
    def get(self, request, loginid):
        
        try:
            # Retrieve the User object associated with the provided loginid
            user = UserTable.objects.get(LOGINID=loginid)

            # Fetch the food orders for the user
            food_orders = FoodorderTable.objects.filter(USERID=user).order_by('-created_at')

            # Serialize the food orders
            food_order_serializer = FoodOrderSerializer(food_orders, many=True)

            return Response(food_order_serializer.data, status=status.HTTP_200_OK)

        except UserTable.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class CancelBooking(APIView):
    def post(self, request, booking_id):
        # Fetch the booking based on booking_id
        booking = get_object_or_404(BookingTable, id=booking_id)
        
        # Check if the booking is already cancelled
        if booking.bookingstatus == 'cancelled':
            return Response({"error": "Booking is already cancelled."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the booking status to 'cancelled'
        booking.bookingstatus = 'cancelled'
        booking.save()

        # Serialize the updated booking data
        booking_serializer = RoomBookingSerializer(booking)
        
        # Return the response with updated booking status
        return Response(booking_serializer.data, status=status.HTTP_200_OK)
    
class FoodMenuView(APIView):
    def get(self, request, restaurant_id):
        try:
            # Fetch all food items for the specific restaurant using the passed restaurant_id
            food_items = FoodmenuTable.objects.filter(RESTAURANTID=restaurant_id)

            # If no food items are found for that restaurant
            if not food_items:
                return Response({"message": "No food items found for this restaurant."}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the data using the FoodmenuSerializer
            serializer = FoodmenuSerializer(food_items, many=True)

            # Return the serialized data as a response with a 200 OK status
            return Response(serializer.data, status=status.HTTP_200_OK)

        except FoodmenuTable.DoesNotExist:
            return Response({"error": "Restaurant or food items not found."}, status=status.HTTP_404_NOT_FOUND)
        

from rest_framework import status  # Ensure the correct import
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FoodorderTable, OrderitemTable, UserTable, FoodmenuTable


class PlaceFoodOrderView(APIView):
    def post(self, request):
        """
        Place a new food order.
        """
        try:
            user_id = request.data.get('USERID')
            menu_id = request.data.get('MENUID')
            quantity = request.data.get('quantity')
            order_status = request.data.get('status', 'pending')  # Default status is 'pending'

            # Retrieve the user and menu objects
            user = UserTable.objects.get(LOGINID=user_id)
            menu = FoodmenuTable.objects.get(id=menu_id)

            # Create a new Orderitem
            order_item = OrderitemTable.objects.create(
                MENUID=menu,
                quantity=quantity,
                status=order_status
            )

            # Create a new Foodorder
            food_order = FoodorderTable.objects.create(
                USERID=user,
                status='pending',  # Default status is 'pending'
                ORDERID=order_item
            )

            # Serialize the food order
            serializer = FoodOrderSerializer(food_order)

            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Correct integer status code

        except UserTable.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)  # Correct integer status code
        except FoodmenuTable.DoesNotExist:
            return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)  # Correct integer status code
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Correct integer status code
        





# Initialize Google Gemini API
genai.configure(api_key="AIzaSyBejqtHHziCWnztalc1eeYmI_NmEa3zgLE")  # Replace with your Gemini API key

# Initialize OpenAI API
# Replace with your OpenAI API key
class ItineraryView(APIView):
    def post(self, request):
        # Get query from the user input
        user_query = request.data.get('query', '')
        budget = request.data.get('budget', 1000)  # Extract budget from the request if provided, default to 1000 INR

        # Default response if no input
        response_data = {
            'rooms': [],
            'rented_vehicles': [],
            'nearby_spots': {
                'free_entry_spots': [],
                'paid_spots': []
            },
            'restaurants': [],
            'chatbot_response': ""  # This will store the chatbot-like response
        }

        # Fetch data from the models and filter based on budget if needed
        rooms_data = RoomTable.objects.filter(price__lte=budget)  # Filter rooms within the user's budget
        rented_vehicles_data = RentedVehicleTable.objects.filter(rent__lte=budget)  # Filter vehicles within the budget
        free_spots_data = SpotTable.objects.filter(ticket="free")  # Get free-entry spots
        paid_spots_data = SpotTable.objects.filter(ticket="paid")  # Get paid spots
        restaurants_data = RestaurantTable.objects.all()  # Get all restaurants (no budget filter for restaurants)

        # Serialize the data to pass it to the Gemini API in a structured way
        rooms_list = RoomTableSerializer(rooms_data, many=True).data
        vehicles_list = RentedVehicleSerializer(rented_vehicles_data, many=True).data
        free_spots_list = SpotSerializer(free_spots_data, many=True).data
        paid_spots_list = SpotSerializer(paid_spots_data, many=True).data
        restaurants_list = RestaurantTableSerializer(restaurants_data, many=True).data

        # Prepare the spots data, adding the ticket charge for paid spots
        paid_spots_info = []
        for spot in paid_spots_list:
            spot_info = {
                "placename": spot['placename'],
                "description": spot['description'],
                "ticket_charge": spot['ticket_charge']
            }
            paid_spots_info.append(spot_info)

        # Construct the prompt using the filtered data (ensure it's only from the models)
        print(user_query,vehicles_list,paid_spots_info,free_spots_list,restaurants_list)
        prompt = (
            f"User Query: {user_query}. "
            f"The available rooms are: {rooms_list}, "
            f"the available rented vehicles are: {vehicles_list}, "
            f"the free-entry spots are: {free_spots_list}, "
            f"the paid spots are: {paid_spots_info}, "
            f"and the restaurants are: {restaurants_list}. "
            f"Include only recommendations from rooms {rooms_list} ,from vehicles {vehicles_list},spots_list{free_spots_list},paid spot_list{paid_spots_info},and{restaurants_list}"
            f"Generate a chatbot-like itinerary for the user within a budget in {user_query} INR. "
            f"Provide the response based on above data if no data is present pls contact admin message should be provided"
        )

        try:
            # Call Gemini API to generate the response
            gemini_response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
            gemini_chatbot_response = gemini_response.text.strip()

            # Update response data with the chatbot response
            response_data['chatbot_response'] = gemini_chatbot_response

            # Return the chatbot-like response with the itinerary data
            return Response(response_data, status=200)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
