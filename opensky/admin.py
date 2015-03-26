from django.contrib import admin
from opensky.models import CarouselImage, Feature, Equipment, Service


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('text', 'position', 'image')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'icon')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'count')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'icon')


admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Service, ServiceAdmin)