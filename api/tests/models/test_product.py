"""
Tests for Product Model
"""
from django.test import TestCase
from api.tests.common import create_product, PRODUCT_NAME, PRODUCT_PRICE


class TestProductModel(TestCase):
    """
    Test the creation of the Product Model
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(TestProductModel, self).setUp()
        self.product = create_product()

    def test_name(self):
        """
        Test that the name of the product is created correctly
        """
        self.assertEqual(self.product.name, PRODUCT_NAME)

    def test_price(self):
        """
        Test that the price of the product is created correctly
        """
        self.assertEqual(self.product.price, PRODUCT_PRICE)

    def test_string_representation(self):
        """
        Test that the string representation of the product is correct
        """
        self.assertEqual(
            str(self.product),
            "{0} @ £{1}".format(PRODUCT_NAME, PRODUCT_PRICE)
        )
