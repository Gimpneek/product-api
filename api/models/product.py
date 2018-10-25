# -*- coding: utf-8 -*-
"""
Model definition of Product
"""
from django.db import models


class Product(models.Model):
    """
    Product model
    """

    name = models.CharField(max_length=256)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=16
    )

    def __str__(self):
        """
        String representation of the Product object
        """
        return "{name} @ £{price}".format(
            name=self.name,
            price=self.price
        )
