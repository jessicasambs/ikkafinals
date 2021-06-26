from django.contrib import admin
from .models import Item, Equipments, Delivery, Payment
# Register your models here.
admin.site.register(Item)
admin.site.register(Equipments)
admin.site.register(Delivery)
admin.site.register(Payment)