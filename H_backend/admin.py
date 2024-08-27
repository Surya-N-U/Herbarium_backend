from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import NewAllPlant

@admin.register(NewAllPlant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'edit_link', 'delete_link')

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', reverse('edit_plant', args=[obj.id]))

    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', reverse('delete_plant', args=[obj.id]))

    def has_add_permission(self, request):
        return False  # Disable add button in admin, use custom upload instead



# Register your models here.
