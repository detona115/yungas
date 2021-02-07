from django.contrib import admin

# Register your models here.
from .models import(
    Pessoa,
    Name,
    Location,
    Coordinate,
    Timezone,    
    Picture,
    Phone,
    Cell
)


admin.site.register(Pessoa)
admin.site.register(Name)
admin.site.register(Location)
admin.site.register(Coordinate)
admin.site.register(Timezone)
admin.site.register(Picture)
admin.site.register(Phone)
admin.site.register(Cell)