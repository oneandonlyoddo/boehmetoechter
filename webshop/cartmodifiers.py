from shop.cart.cart_modifiers_base import BaseCartModifier
from decimal import Decimal

class ShippingDHL(BaseCartModifier):

    def get_extra_cart_price_field(self, cart, request):
        shipping = Decimal('6.90')
        return ('Versand mit DHL', shipping)
        
class PreisOhneMehrwertsteuer(BaseCartModifier):
   
    def get_extra_cart_price_field(self, cart, request):
        nineten_percent = Decimal('19') / Decimal('100')
        # Now we need the current cart total. It's not just the subtotal field
        # because there may be other modifiers before this one
        total = cart.current_total
        mehrwertsteuer = total * nineten_percent
        mehrwertsteuer = - mehrwertsteuer # a rebate is a negative difference
        return ('Nettosumme', mehrwertsteuer)

class PreisMitMehrwertsteuer(BaseCartModifier):
   
    def get_extra_cart_price_field(self, cart, request):
        nineten_percent = Decimal('19') / Decimal('100')
        # Now we need the current cart total. It's not just the subtotal field
        # because there may be other modifiers before this one
        total = cart.current_total
        mehrwertsteuer = total * nineten_percent
        return ('Bruttosumme', mehrwertsteuer)
        