from django.contrib import admin
from .models import Property, ContactMessage, Newsletter


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'listing_type', 'price', 'city', 'is_featured', 'created_at']
    list_filter = ['listing_type', 'property_type', 'is_featured', 'city']
    search_fields = ['title', 'address', 'city']
    list_editable = ['is_featured']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email']
    list_editable = ['is_read']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']
