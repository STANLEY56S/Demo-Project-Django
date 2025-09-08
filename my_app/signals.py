from .models import Auth, Category, Item
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = Category)
def django_signals(sender, instance, created, **kwargs):
    if created:
        print(sender.__name__)
        # print(sender.__name__)
        print("--------")
        print(instance.name)