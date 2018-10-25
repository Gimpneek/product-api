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
    pagination_class = None

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
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(ProductViewSet, self).get_serializer(*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Override DELETE to return 200 as defined in test

        :param request: Django request
        :return: Django Response
        """
        super(ProductViewSet, self).destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)
