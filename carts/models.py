from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from products.models import ProductVariant


class Item(models.Model):
    cart = models.ForeignKey('Cart', verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    product = models.ForeignKey(ProductVariant)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def total_price(self):
        return self.quantity * self.unit_price


class CartQuerySet(models.QuerySet):

    def get_cart_from_request(self, request):
        return self.get_or_create(user=request.user)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    objects = CartQuerySet.as_manager()

    def update_cart(self, productvarid, qty):

        prod = ProductVariant.objects.get(pk=productvarid)
        self.item_set.create(product=prod, quantity=qty)

    def __unicode__(self):
        return "Cart-%s" % (self.id)
