from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sale/', views.sale_view, name='sale'),
    path('production/', views.production_view, name='production'),
    # path('spoiled/', views.spoiled_view, name='spoiled'),  # Removed
    path('expense/', views.expense_view, name='expense'),
    path('feed/', views.feed_view, name='Feed'),
    path('livestock/', views.livestock_view, name='Livestock'),
    path('inventory/', views.inventory_view, name='Inventory'),
]
