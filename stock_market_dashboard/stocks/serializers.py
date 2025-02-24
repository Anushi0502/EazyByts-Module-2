from django.contrib.auth.models import User
from .models import Stock, Portfolio

# Define serializers for the models without using REST framework

class StockSerializer:
    def __init__(self, stock):
        self.stock = stock

    def to_dict(self):
        return {
            'id': self.stock.id,
            'name': self.stock.name,
            'symbol': self.stock.symbol,
            'price': str(self.stock.price),
            'last_updated': self.stock.last_updated.isoformat(),
        }

class PortfolioSerializer:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def to_dict(self):
        return {
            'id': self.portfolio.id,
            'user': self.portfolio.user.username,
            'stocks': [StockSerializer(stock).to_dict() for stock in self.portfolio.stocks.all()],
        }
