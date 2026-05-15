from django.contrib import admin
from .models import OccasionMessage

# Register your models here
@admin.register(OccasionMessage)
class OccasionMessageAdmin(admin.ModelAdmin):
    list_display = ['occasion', 'title', 'theme_color', 'emojis']
    list_editable = ['title', 'theme_color', 'emojis']
    search_fields = ['occasion', 'title']
    list_filter = ['occasion']