from django.db import models

class OptionItem(models.Model):
    date_insertion = models.DateField(default=None)
    option_code = models.CharField(max_length=50, default='')
    option_type = models.CharField(max_length=50)
    underlying_asset = models.CharField(max_length=50) 
    expiration_date = models.DateField(default=None)
    strike_price = models.DecimalField(max_digits=15, decimal_places=4)
