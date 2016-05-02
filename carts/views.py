from rest_framework.response import Response
from rest_framework.views import APIView
from carts.models import Cart
from carts.serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated


class CartViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            cart = Cart.objects.get(user=request.user)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except:
            return Response({})