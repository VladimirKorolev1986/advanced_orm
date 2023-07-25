from django.shortcuts import render

from demo.models import Order


# Create your views here.

def list_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context=context)
