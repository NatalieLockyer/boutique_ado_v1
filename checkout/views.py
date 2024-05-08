from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PE3lnRvGkLgnhhbCdwCkmCVmtlKQtrs1359FinceIGRjaDs8d8CqnCB5UdPa1bgfuykLAHsb31boH8JLad4An4g00dmIF9p5X',
        'client_secret': 'test client secret',
        }

    return render(request, template, context)