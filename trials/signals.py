from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Subscription,Channel,Bouquet

# @receiver(post_save, sender=User)