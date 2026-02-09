from django.contrib import admin
from .models import Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_start', 'is_featured', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_featured',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'created_at')
    list_filter = ('rating',)
