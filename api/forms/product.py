# pylint: disable=useless-object-inheritance
"""
Form for Product model
"""
from django.forms.models import ModelForm
from api.models.product import Product


class ProductForm(ModelForm):
    """
    Product Form
    """

    class Meta(object):
        """
        Metaclass for Product Form
        """
        model = Product
        fields = (
            'name',
            'price'
        )
