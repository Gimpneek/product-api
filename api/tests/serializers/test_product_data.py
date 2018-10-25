""" Test the data representation of the Product API """
from api.tests.common import ProductAPICase, PRODUCTS_URL


class TestProductCollection(ProductAPICase):
    """
    Test the data returned by the Product collection endpoint
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(TestProductCollection, self).setUp()
        resp = self.api.get(PRODUCTS_URL)
        self.result = resp.data.get('results')[0]

    def test_id(self):
        """
        Test that the id for the product is returned correctly
        """
        self.assertEqual(self.result.get('id'), self.product.id)

    def test_name(self):
        """
        Test that the name for the product is returned correctly
        """
        self.assertEqual(self.result.get('name'), self.product.name)

    def test_price(self):
        """
        Test that price for the product is return correctly
        """
        self.assertEqual(self.result.get('price'), self.product.price)


class TestProductResource(ProductAPICase):
    """
    Test the data returned by the Product resource endpoint
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(TestProductResource, self).setUp()
        resp = self.api.get("{0}/{1}".format(PRODUCTS_URL, self.product.id))
        self.result = resp.data

    def test_id(self):
        """
        Test that the id for the product is returned correctly
        """
        self.assertEqual(self.result.get('id'), self.product.id)

    def test_name(self):
        """
        Test that the name for the product is returned correctly
        """
        self.assertEqual(self.result.get('name'), self.product.name)

    def test_price(self):
        """
        Test that price for the product is return correctly
        """
        self.assertEqual(self.result.get('price'), self.product.price)
