"""
Test the HTTP verbs of the Product view set
"""
from api.tests.common import ProductAPICase, PRODUCTS_URL
from api.models.product import Product


class TestProductCollection(ProductAPICase):
    """
    Test the HTTP verbs of the collection views
    """

    def setUp(self):
        """
        Set up test
        """
        super(TestProductCollection, self).setUp()
        self.url = PRODUCTS_URL

    def test_get(self):
        """
        Test the user is able to get a list of products
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        """
        Test the user is able to create a new product
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Satan',
                'price': 6.66
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_post_creates_product(self):
        """
        Test that call to POST creates a product
        """
        self.api.post(
            self.url,
            {
                'name': 'Satan',
                'price': 6.66
            }
        )
        product = Product.objects.get(name='Satan')
        self.assertEqual(
            str(product.price),
            '6.66'
        )

    def test_post_error(self):
        """
        Test the user is returned a 400 when sending bad data
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Badness',
                'price': 'some money'
            }
        )
        self.assertEqual(resp.status_code, 400)

    def test_post_partial(self):
        """
        Test the user is returned 400 when sending partial data
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Satan'
            }
        )
        self.assertEqual(resp.status_code, 400)

    def test_delete(self):
        """
        Test the user is return a 405 when sending DELETE verb
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_put(self):
        """
        Test the user is return a 405 when sending PUT verb
        """
        resp = self.api.put(
            self.url,
            {
                'name': 'Satan',
                'price': 6.66
            }
        )
        self.assertEqual(resp.status_code, 405)


class TestProductResource(ProductAPICase):
    """
    Test the resource verbs of the Product
    """

    def setUp(self):
        super(TestProductResource, self).setUp()
        self.url = '{0}/{1}'.format(PRODUCTS_URL, self.product.id)

    def test_get(self):
        """
        Test the user is able to get a product
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_not_found(self):
        """
        Test the user is returned a 404 when the ID provided isn't in the
        system
        """
        resp = self.api.get('{0}/{1}'.format(PRODUCTS_URL, 666))
        self.assertEqual(resp.status_code, 404)

    def test_post(self):
        """
        Test that POST returns a 405
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Satan',
                'price': 6.66
            }
        )
        self.assertEqual(resp.status_code, 405)

    def test_delete(self):
        """
        Test that DELETE removes the Product
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_delete_removes_record(self):
        """
        Test that DELETE removes the Product
        """
        self.api.delete(self.url)
        product = Product.objects.filter(pk=self.product.id)
        self.assertEqual(len(product), 0)

    def test_delete_not_found(self):
        """
        Test the user is returned a 404 when the ID provided isn't in the
        system
        """
        resp = self.api.delete('{0}/{1}'.format(PRODUCTS_URL, 666))
        self.assertEqual(resp.status_code, 404)

    def test_put(self):
        """
        Test that when sending the correct data that PUT is successful
        """
        resp = self.api.put(
            self.url,
            {
                'name': 'Satan'
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_put_updates_product(self):
        """
        Test that PUT updates the record
        """
        self.api.put(
            self.url,
            {
                'name': 'Satan'
            }
        )
        product = Product.objects.get(name='Satan')
        self.assertEqual(product.price, self.product.price)

    def test_put_error(self):
        """
        Test that when sending incorrect data that PUT fails
        """
        resp = self.api.put(
            self.url,
            {
                'price': 'some money'
            }
        )
        self.assertEqual(resp.status_code, 400)

    def test_put_not_found(self):
        """
        Test the user is returned a 404 when the ID provided isn't in the
        system
        """
        resp = self.api.put(
            '{0}/{1}'.format(PRODUCTS_URL, 666),
            {
                'name': 'Satan'
            }
        )
        self.assertEqual(resp.status_code, 404)
