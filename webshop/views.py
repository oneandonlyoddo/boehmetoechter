from django.views.generic import DetailView, TemplateView, ListView
from shop.util.cart import get_cart_from_session
from shop.views.product import ProductDetailView
from django.shortcuts import get_object_or_404
from shop.models.productmodel import Product
from models import LageKategorie, ArtKategorie
from django.db.models import Q

class MyShopListView(ListView):
    """
    This is just to abstract the "Django version switching magic happening up
    there
    """
    def get_queryset(self):
       
        

        return Product.objects.filter(listed=True).order_by('art__sortID', 'kat__sortID','slug')
    
    def get_context_data(self, **kwargs):
     
        ctx = super(MyShopListView, self).get_context_data(**kwargs)

        cart = get_cart_from_session(self.request)
        
        if cart is not None:
            cart.update(self.request)
            ctx.update({'cart': cart})

        return ctx

    class Meta:
        pass

class MyProductDetailView(ProductDetailView):
    """
    This is just to abstract the "Django version switching magic happening up
    there
    """
    
    def get_context_data(self, **kwargs):
     
        
        ctx = super(MyProductDetailView, self).get_context_data(**kwargs)

        cart = get_cart_from_session(self.request)
        if cart is not None:
            cart.update(self.request)
            ctx.update({'cart': cart})

        return ctx


    class Meta:
        pass

class KatView(ListView):
    """
    This is just to abstract the "Django version switching magic happening up
    there
    """

    template_name = "singleKat_list.html"
    def get_queryset(self):
       
        
        self.name=self.args[0]

        return Product.objects.filter(Q(kat__slug=self.name)|Q(art__slug=self.name))

    def get_context_data(self, **kwargs):
        
        ctx = super(KatView, self).get_context_data(**kwargs)
        categoryProducts = Product.objects.filter(kat__slug=self.args[0])
        
        cart = get_cart_from_session(self.request)
        if cart is not None:
            cart.update(self.request)
        ctx.update(
            {'cart': cart,
            'category': categoryProducts,
            })
        return ctx

    class Meta:
        pass


class KatView2(TemplateView):
   

    template_name = "singleKat_list.html"
    

    def get_context_data(self, **kwargs):
        
        ctx = super(KatView2, self).get_context_data(**kwargs)
        self.name=self.args[0]
        
        product_list = Product.objects.filter(listed=True).filter(Q(kat__slug=self.name)|Q(art__slug=self.name)).order_by('art__sortID')
        category = LageKategorie.objects.filter(slug=self.args[0])
        art = ArtKategorie.objects.filter(slug=self.args[0])
        cart = get_cart_from_session(self.request)
        if cart is not None:
            cart.update(self.request)
        ctx.update(
            {'cart': cart,
            'product_list': product_list,
            'category': category,
            'art': art,
            })
        return ctx

    class Meta:
        pass

class DoubleKatView(ListView):
    """
    This is just to abstract the "Django version switching magic happening up
    there
    """
    template_name = "doubleKat_list.html"
    def get_queryset(self):
       
        
        self.name1=self.args[0]
        self.name2=self.args[1]

        return Product.objects.filter(Q(kat__slug=self.name1 ,art__slug=self.name2)|Q(kat__slug=self.name2 ,art__slug=self.name1))

    def get_context_data(self, **kwargs):
        
        ctx = super(DoubleKatView, self).get_context_data(**kwargs)

        cart = get_cart_from_session(self.request)
        if cart is not None:
            cart.update(self.request)
        ctx.update({'cart': cart})
        return ctx

    class Meta:
        pass