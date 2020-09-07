from celery.task import task
from stocks.models import Stock


@task()
def price_update(name="price_update"):

    print('--- Started ---')
    stocks = Stock.objects.all()

    for stock in stocks:
        stock.current_price += 200
        stock.save()
        print(stock.current_price)

    print('--- Completed ---')
