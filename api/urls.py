"""
URLS for api module
"""
from django.conf.urls import url, include
from rest_framework import routers
from api.view_sets.product import ProductViewSet


API_ROUTER = routers.SimpleRouter(trailing_slash=False)
API_ROUTER.register(r'products', ProductViewSet, base_name='products')
API_ROUTER.register(r'product', ProductViewSet, base_name='product')

urlpatterns = [
    url('v1/', include(API_ROUTER.urls)),
]

API_URLS = urlpatterns, 'api', 'api'
