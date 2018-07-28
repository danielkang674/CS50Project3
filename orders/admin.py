from django.contrib import admin
from .models import Size, PizzaTopping, Pizza, SubTopping, Sub, Pasta, Salad, Platter, PizzaStyle, PizzaType, SubType, PlatterType

# Register your models here.

admin.site.register(Size)
admin.site.register(PizzaStyle)
admin.site.register(PizzaType)
admin.site.register(SubType)
admin.site.register(PizzaTopping)
admin.site.register(Pizza)
admin.site.register(SubTopping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(PlatterType)
admin.site.register(Platter)