from .models import Stock
from .serializers import StockSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Handles Datasets - DatasetResource & DatasetTags belong to Datasets.
    """
    permission_classes = [AllowAny]
    serializer_class = StockSerializer
    queryset = Stock.objects.filter(active=True)
    pagination_class = None
