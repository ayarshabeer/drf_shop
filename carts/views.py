from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from carts.models import Cart
from cart.serializer import CartSerializer


@api_view('POST')
@permission_classes((IsAuthenticated, ))
def add_to_cart(request, format=None):
    productvar_id = request.data['product']
    qty = request.data['qty']
    cart = Cart.objects.get_cart_from_request(request)
    cart.update_cart(productvar_id, qty)
    serializer = CartSerializer(cart)
    return Response(serializer.data)
