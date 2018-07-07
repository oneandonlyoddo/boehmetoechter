from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import Wein, myOrder, LageKategorie, ArtKategorie, LagenKatForm, ArtKatForm, GeschmacksrichtungKatForm, GeschmacksrichtungKategorie, WeinForm, QualitaetKategorie, QualitaetKatForm


from shop.admin.mixins import LocalizeDecimalFieldsMixin
from shop.order_signals import completed
from django.utils.translation import ugettext_lazy as _
from shop.models.ordermodel import (OrderItem,
        OrderExtraInfo, ExtraOrderPriceField, OrderPayment)

class OrderExtraInfoInline(admin.TabularInline):
    model = OrderExtraInfo
    extra = 0


class OrderPaymentInline(LocalizeDecimalFieldsMixin, admin.TabularInline):
    model = OrderPayment
    extra = 0


class ExtraOrderPriceFieldInline(LocalizeDecimalFieldsMixin, admin.TabularInline):
    model = ExtraOrderPriceField
    extra = 0


class OrderItemInline(LocalizeDecimalFieldsMixin, admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ('product',)

#TODO: add ExtraOrderItemPriceField inline, ideas?

class Kat_Admin( admin.ModelAdmin ):
    form = LagenKatForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'sortID')

class Art_Admin( admin.ModelAdmin ):
    form = ArtKatForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'sortID')

class Geschmack_Admin( admin.ModelAdmin ):
    form = GeschmacksrichtungKatForm
    #prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

class Qualitaet_Admin( admin.ModelAdmin ):
    form = QualitaetKatForm
    #prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

class Wein_Admin( admin.ModelAdmin ):
    form = WeinForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'jahrgang','art','kat', 'active','listed')

class OrderAdmin(LocalizeDecimalFieldsMixin, ModelAdmin):
    list_display = ('id', 'shipPrename', 'shipSurname','status', 'order_total', 'created')
    list_filter = ('status', 'user')
    search_fields = ('id', 'shipping_address_text', 'shipSurname')
    date_hierarchy = 'created'
    inlines = (OrderItemInline, OrderExtraInfoInline,
            ExtraOrderPriceFieldInline, OrderPaymentInline)
    readonly_fields = ('created', 'modified',)
    fieldsets = (
            (None, {'fields': ( 'status', 'order_total',
                'order_subtotal', 'created', 'modified')}),
            (_('Shipping'), {
                'fields': ('shipping_address_text',),
                }),
            (_('Billing'), {
                'fields': ('billing_address_text',)
                }),
            )

    def save_model(self, request, order, form, change):
        super(OrderAdmin, self).save_model(request, order, form, change)
        if not order.is_completed() and order.is_paid():
            order.status = Order.COMPLETED
            order.save()
            completed.send(sender=self, order=order)

admin.site.register(LageKategorie, Kat_Admin)
admin.site.register(ArtKategorie, Art_Admin)
admin.site.register(GeschmacksrichtungKategorie, Geschmack_Admin)
admin.site.register(QualitaetKategorie, Qualitaet_Admin)
admin.site.register(Wein, Wein_Admin)
admin.site.register(myOrder, OrderAdmin)





