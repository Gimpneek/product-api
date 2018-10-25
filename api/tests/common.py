"""
Common Test Data Creation Functions
"""
from django.test import TestCase
from rest_framework.test import APIClient
from api.models.product import Product

PRODUCT_NAME = 'Lavender Heart'
PRODUCT_PRICE = 9.25
PRODUCTS_URL = '/v1/products'


def create_product(name=None, price=None):
    """
    Create a product, if no values are provided use the defaults

    :param name: Name of the product
    :param price: Price of the product
    :return: newly created Product instance
    """
    if not name:
        name = PRODUCT_NAME
    if not price:
        price = PRODUCT_PRICE
    return Product.objects.create(
        name=name,
        price=price
    )


class ProductAPICase(TestCase):
    """
    Common setup for Product API tests
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(ProductAPICase, self).setUp()
        self.product = create_product()
        self.api = APIClient()
