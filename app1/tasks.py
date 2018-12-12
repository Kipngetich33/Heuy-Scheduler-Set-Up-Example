from myproject2.settings import HUEY as huey
from datetime import datetime
from huey import crontab
from .models import My_Test_Model

@huey.periodic_task(crontab(minute='*/1'))
def testapp_1():
    # add one
    old = My_Test_Model.objects.last()
    old.amount = old.amount + 1
    old.save()
    print "Task Done"