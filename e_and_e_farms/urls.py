from django.contrib import admin
from django.urls import path
from milk import views as milk_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', milk_views.home_view, name='home'),
    path('sale/', milk_views.sale_view, name='sale'),
    path('production/', milk_views.production_view, name='production'),
    path('expense/', milk_views.expense_view, name='expense'),
    path('feed/', milk_views.feed_view, name='Feed'),
    path('livestock/', milk_views.livestock_view, name='Livestock'),
    path('inventory/', milk_views.inventory_view, name='Inventory'),
]
