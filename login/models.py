from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Data(models.Model):
    Choices =(
        ('iron','IRON'),
        ('nitrate', 'NITRATE'),
        ('salinity', 'SALINITY'),
        ('fluoride', 'FLUORIDE'),
        ('arsenic', 'ARSENIC')
    )

    District = models.CharField(max_length=50)
    Block = models.CharField(max_length=50)
    Panchayat = models.CharField(max_length=50)
    Village = models.CharField(max_length=50)
    Habitation = models.CharField(max_length=50)
    Parameter = models.CharField(max_length=10, choices=Choices, default='iron')
    Permissible_limit = models.DecimalField(max_digits=6, decimal_places=5)
    Actual_level = models.DecimalField(max_digits=6,decimal_places=5)

