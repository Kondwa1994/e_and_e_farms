
from django.shortcuts import render, redirect
from .models import Sale
from collections import defaultdict
from .forms import SaleForm
from django.utils.timezone import now  # import timezone aware date

def home_view(request):
    return render(request, 'home.html')


def sale_view(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale')
    else:
        # Set initial date to today
        form = SaleForm(initial={'date': now().date()})

    sales = Sale.objects.all().order_by('-date')
    sales_by_date = defaultdict(list)
    daily_totals = {}

    for sale in sales:
        amount = sale.total_sale
        sales_by_date[sale.date].append({
            'customer': sale.customer,
            'litres_sold': sale.litres_sold,
            'price_per_litre': sale.price_per_litre,
            'paid': sale.paid,
            'amount': amount,
        })
        daily_totals[sale.date] = daily_totals.get(sale.date, 0) + amount

    has_unpaid = any(sale.paid < sale.total_sale for sale in sales)

    context = {
        'form': form,
        'sales_by_date': sales_by_date,
        'daily_totals': daily_totals,
        'has_unpaid': has_unpaid,
    }
    return render(request, 'sale.html', context)


def production_view(request):
    return render(request, 'production.html')

def expense_view(request):
    return render(request, 'expense.html')

def feed_view(request):
    return render(request, 'feed.html')

def livestock_view(request):
    return render(request, 'livestock.html')

def inventory_view(request):
    return render(request, 'inventory.html')
