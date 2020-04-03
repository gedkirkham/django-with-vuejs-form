from vuejsform.models import Product
from rest_framework import viewsets
from vuejsform.serialiser import ProductSerialiser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser