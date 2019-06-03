from django.contrib import admin

from main.models.order import Order
from main.models.reviews import Reviews


class ListedOrders(admin.ModelAdmin):
    list_filter = ('order_date', 'costs', 'is_finished', 'user')
    list_display = ('is_finished', 'user', 'died', 'coffin', 'flowers', 'music', 'order_date', 'costs')


class ListedReviews(admin.ModelAdmin):
    list_filter = ('rating', 'user', 'date_added')


admin.site.register(Order, ListedOrders)
admin.site.register(Reviews, ListedReviews)
