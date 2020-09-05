from rest_framework import serializers as s
from .models import Stock


class StockSerializer(s.ModelSerializer):

    #  We make things read-only, here
    def __init__(self, *args, **kwargs):
        super(StockSerializer, self).__init__(*args, **kwargs)
        setattr(self.Meta, 'read_only_fields', [*self.fields])

    class Meta:
        model = Stock
        fields = [
            'active',
            'pk',
            'symbol',
            'name',
            'sector',
            'base_price',
            'ceiling_price',
            'lowest_price',
            'highest_price',
            'current_price',
            'booming',
            'busting',
            'suspended',
            'spiked_dropped',
        ]

