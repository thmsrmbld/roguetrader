import uuid

from django.db import models
from roguetrader.base_classes import CreatedUpdated


class Stock(CreatedUpdated):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    symbol = models.CharField(
        max_length=3
    )

    name = models.CharField(
        max_length=30
    )

    sector = models.ForeignKey(
        'MarketSector',
        on_delete=models.SET_NULL,
        null=True,
    )

    # Each stock has its own inherent baseline value
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    ceiling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    lowest_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    highest_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    # This illustrates how long in 'turns' a stock has left on an ASCENDING trend series and it auto-decrements
    booming = models.PositiveIntegerField(
        null=False,
        default=0,
    )

    # This illustrates how long in 'turns' a stock has left on a DESCENDING trend series and it auto-decrements
    busting = models.PositiveIntegerField(
        null=False,
        default=0
    )

    suspended = models.PositiveIntegerField(
        null=False,
        default=0
    )

    # The stock has been randomly spiked or dropped during the previous iteration
    spiked_dropped = models.BooleanField(
        default=False,
    )

    active = models.BooleanField(
        default=False,
    )

    # Lets keep some logic low in the stack
    def is_suspended(self):
        if self.suspended > 0:
            return True

    def is_booming(self):
        if self.booming > 0:
            return True

    def is_busting(self):
        if self.busting > 0:
            return True

    def decrement_trend(self):
        if self.is_suspended():
            self.suspended -= 1
            print(f'{self.name} is still suspended for {self.suspended} iterations')
            self.save()

        elif self.is_busting():
            self.busting -= 1
            print(f'{self.name} is still busting for {self.busting} iterations')
            self.save()

        elif self.is_booming():
            self.booming -= 1
            print(f'{self.name} is still booming for {self.booming} iterations')
            self.save()

        return self

    # Django specific overrides/metas
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class MarketSector(CreatedUpdated):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        # choices=SECTOR_TYPES,
        max_length=60,
        null=True
    )

    spiked_dropped = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
