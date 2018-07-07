from shop.cart.cart_modifiers_base import BaseCartModifier

class MyModifier(BaseCartModifier):
    """
    An example class that will grant a 10% discount to shoppers who buy
    more than 500 worth of goods.
    """
    def get_extra_cart_price_field(self, cart, request):
        shipping = 6,90
        # Now we need the current cart total. It's not just the subtotal field
        # because there may be other modifiers before this one
        total = cart.current_total + shipping
        # extra_dict = { 'Versandkosten': '%s %%' % ten_percent }
        return ('Versand mit DHL', total)
        