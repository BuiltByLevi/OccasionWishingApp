from django.contrib import admin
from .models import OccasionMessage, FriendWish

@admin.register(OccasionMessage)
class OccasionMessageAdmin(admin.ModelAdmin):
    list_display = ['occasion', 'title', 'theme_color', 'emojis']
    list_editable = ['title', 'theme_color', 'emojis']
    search_fields = ['occasion', 'title']

@admin.register(FriendWish)
class FriendWishAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'added_date']
    search_fields = ['name']
    list_filter = ['added_date']