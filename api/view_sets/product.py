# pylint: disable=too-many-ancestors
"""
View Set for Product Serializer
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.forms.product import ProductForm
from api.models.product import Product
from api.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    View Set for Image Serializer
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        """
        Create a Product

        :param request: Django Request
        :return: Django Response
        """
        form = ProductForm(request.POST, request.data)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data.get('name'),
                price=form.cleaned_data.get('price')
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ProductViewSet, self).get_serializer(*args, **kwargs)
