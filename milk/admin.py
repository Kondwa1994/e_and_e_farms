from django.contrib import admin
from .models import MilkProduction, Sale, Expense, SpoiledMilk

admin.site.register(MilkProduction)
admin.site.register(Sale)
admin.site.register(Expense)
admin.site.register(SpoiledMilk)
