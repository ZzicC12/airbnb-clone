from django.contrib import admin
from . import models


@admin.register(models.RoomType)
class RoomType(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class Room(admin.ModelAdmin):
    pass
