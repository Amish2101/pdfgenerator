from django.db.models.signals import post_save, pre_save
from user.models import cbcreport


def save_signal(sender, instance, created, **kwargs):
    print("hello")
    x = instance.cbcreport
    print("hello")
    print("hello",x)
        
post_save.connect(save_signal, sender=cbcreport)
# pre_save.connect(save_signal, sender=cbcreport)