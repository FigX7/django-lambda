from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers

from _product import models
from _product import serializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing website objects.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.AllowAny]


product_router = routers.SimpleRouter()
product_router.register('', ProductViewSet, basename='products')
