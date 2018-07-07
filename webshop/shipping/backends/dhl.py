# -*- coding: utf-8 -*-
from decimal import Decimal
from shop.util.order import get_order_from_request
from shop.util.cart import get_cart_from_session
from django.conf import settings
from django.conf.urls import patterns, url
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.utils.translation import ugettext_lazy as _

from shop.util.decorators import on_method, shop_login_required, order_required


class ShippingDHL(object):
    """
    This is just an example of a possible flat-rate shipping module, that
    charges a flat rate defined in settings.SHOP_SHIPPING_FLAT_RATE
    """
    url_namespace = 'dhl'
    backend_name = 'DHL'
    backend_verbose_name = _('DHL')

    def __init__(self, shop):
        self.shop = shop  # This is the shop reference, it allows this backend
        # to interact with it in a tidy way (look ma', no imports!)
        self.rate = getattr(settings, 'SHOP_SHIPPING_FLAT_RATE', '0')
        

    @on_method(shop_login_required)
    @on_method(order_required)
    def view_process_order(self, request):
        """
        A simple (not class-based) view to process an order.

        This will be called by the selection view (from the template) to do the
        actual processing of the order (the previous view displayed a summary).

        It calls shop.finished() to go to the next step in the checkout
        process.
        """
        self.shop.add_shipping_costs(self.shop.get_order(request),
                                     'Versand mit DHL',
                                     #Decimal(self.rate))
                                    self.get_shipping_cost(get_cart_from_session(request)))
        return self.shop.finished(self.shop.get_order(request))
        # That's an HttpResponseRedirect

    @on_method(shop_login_required)
    @on_method(order_required)
    def view_display_fees(self, request):
        """
        A simple, normal view that displays a template showing how much the
        shipping will be (it's an example, alright)
        """
        ctx = {}
        #ctx = super(ShippingDHL, self).get_context_data(**kwargs)
        order = get_order_from_request(request)
        cart = get_cart_from_session(request)
        ctx.update({'shipping_costs': self.get_shipping_cost(cart),
            #'shipping_costs': Decimal(self.rate),
            'order': order,
            'cart': cart,
        })
        return render_to_response('shop/shipping/flat_rate/display_fees.html',
            ctx, context_instance=RequestContext(request))

    def get_urls(self):
        """
        Return the list of URLs defined here.
        """
        urlpatterns = patterns('',
            url(r'^$', self.view_display_fees, name='dhl'),
            url(r'^process/$', self.view_process_order, name='flat_process'),
        )
        return urlpatterns

    def get_shipping_cost(self, cart):
        self.cart = cart
        total = cart.total_quantity
        if total >= Decimal('60'):
        	return Decimal('0.00')
        elif total >= Decimal('43'):
        	return Decimal('15.00')
        elif total >= Decimal('22'):
        	return Decimal('10.00')
        elif total >= Decimal('18'):
        	return Decimal('5.00')
        elif total >= Decimal('3'):
        	return Decimal('9.50')
        elif total < Decimal('3'):
        	return Decimal('5.00')            