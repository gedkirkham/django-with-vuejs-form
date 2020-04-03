from rest_framework import routers
from .viewsets import ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'product', ProductViewSet)