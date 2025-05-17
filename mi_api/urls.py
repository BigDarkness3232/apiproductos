from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'producto')

urlpatterns = router.urls