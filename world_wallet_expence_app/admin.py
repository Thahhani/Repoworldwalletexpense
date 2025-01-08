from django.contrib import admin

from world_wallet_expence_app.models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(WalletTable)
admin.site.register(TransactionTable)
admin.site.register(RoomTable)
admin.site.register(BookingTable)
admin.site.register(RestaurantTable)
admin.site.register(RoomComplaintTable)
admin.site.register(RestaurantComplaintTable)
admin.site.register(FeedbackTableforRestaurant)
admin.site.register(FeedbackTableforRoom)
admin.site.register(FoodmenuTable)
admin.site.register(FoodorderTable)
admin.site.register(OrderitemTable)
admin.site.register(ExpenseTable)
admin.site.register(Notification)
admin.site.register(RentedVehicleTable)
admin.site.register(SpotTable)

