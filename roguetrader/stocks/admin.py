from django.contrib import admin
from .models import Stock, MarketSector


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'active',
        'symbol',
        'sector',
        'current_price',
        'highest_price',
        'lowest_price',
        'base_price',
        'suspended',
        'busting',
        'booming',
        'spiked_dropped',
        'updated'
    ]

    list_editable = [
        'active',
        'current_price',
        'sector',
        'base_price',
        'busting',
        'booming',
        'spiked_dropped',
        'suspended'
    ]


@admin.register(MarketSector)
class MarketSector(admin.ModelAdmin):
    list_display = [
        'name',
        'spiked_dropped'
    ]

    list_editable = ['spiked_dropped']

