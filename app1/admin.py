from django.contrib import admin
from app1.models import Booking
from app1.models import contact
# Register your models here.

class bookingadmin(admin.ModelAdmin):
    list_display=['name','where','guest','arrivals','leaving']
admin.site.register(Booking,bookingadmin)

class contactadmin(admin.ModelAdmin):
    list_display=['name','email','number','subject','message']
admin.site.register(contact,contactadmin)