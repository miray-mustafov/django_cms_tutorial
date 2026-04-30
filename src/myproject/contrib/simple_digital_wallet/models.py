from django.db import models
from cms.models import CMSPlugin


class SimpleDigitalWalletPlugin(CMSPlugin):
    holder_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
