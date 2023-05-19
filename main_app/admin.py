from django.contrib import admin

from .models import Restaurant, YourOrder, Tag

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(YourOrder)
admin.site.register(Tag)