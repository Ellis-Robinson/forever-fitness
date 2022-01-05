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
        'stripe_public_key': 'pk_test_51K47v3KmEBOEpD6dbrC28cHloodjANrlnRreChvj7lhy79Hqznsuptn65pVRAI92sT4bxJIKI1w7z5kUeaMn17wx00OL17fr9U'
    }

    return render(request, template, context)


# Create your views here.
