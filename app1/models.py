from __future__ import unicode_literals

from django.db import models

# Create your models here.
class My_Test_Model(models.Model):
    '''
    class that defines the structure of each profile object
    '''
    amount = models.IntegerField()
    record_date = models.DateTimeField(auto_now_add=True, null= True, blank = True)