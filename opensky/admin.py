from django.contrib import admin
from opensky.models import *

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('text', 'position', 'image')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'count')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'photo')

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('address', 'email')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('mark', 'text')

@admin.register(SocialWidget)
class SocialWidgetAdmin(admin.ModelAdmin):
    list_display = ('mark', 'logo', 'url')