
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed

import uuid

DEPARTMENT_CHOICES = (
    ("RECEPTION", "Receptionist"),
    ("COLLECTOR", "Collection"),
    ("SETUP", "Fixer"),
    
)
TYPES =  (
    ("1", "Cable"),
    ("2", "Broadband"),
)

STATUS =  (
    ("1", "OPEN"),
    ("2", "CLOSED"),
    ("3","FAILED"),
    ("4","PENDING"),
)

TICKET =  (
    ("1", "AUDIO"),
    ("2", "MESSAGE"),
    ("3","PICTURE"),
)
# Create your models here.
# class User(AbstractUser):

#     pass


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField("CODE", max_length=1000, default=None, blank=True, null=True)
    description = models.CharField("DESCRIPTION", max_length=1000, default=None, blank=True, null=True)
    def __str__(self):
        return self.code

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("NAME OF THE DEVICE", max_length=1000, default=None, blank=True, null=True)
    iemi_number = models.BigIntegerField( "IEMI NUMBER", default=None, blank=True, null=True)
    service_provider = models.TextField("NETWORK PROVIDER", max_length=1000, default=None, blank=True, null=True)
    def __str__(self):
        return self.name


class User(AbstractUser):
    address = models.TextField("ADDRESS", max_length=1000, default=None, blank=True, null=True)
    pincode = models.IntegerField("Zip Code", default=None, blank=True, null=True)
    phone_number = models.CharField("PHONE NUMBER", max_length=20, default=None, blank=True, null=True)
    alternate_number = models.CharField(" ALTERNATE PHONE NUMBER", max_length=20, default=None, blank=True, null=True)
    gst = models.CharField("GST NUMBER ", max_length=1000, default=None, blank=True, null=True)
    zone = models.CharField("ZONE", max_length=1000, default=None, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL , blank=True, null=True)
    department = models.CharField("DEPARTMENT (staff)", max_length=1000, choices=DEPARTMENT_CHOICES,  default=None, blank=True, null=True)
    assigned_devices = models.ForeignKey(Device, on_delete=models.SET_NULL , blank=True, null=True)
    mpos_serial_number = models.CharField("MPOS SERIAL NUMBER (staff)", max_length=1000, default=None, blank=True, null=True)
    mpos_user_name = models.CharField("MPOS USER NAME", max_length=1000, default=None, blank=True, null=True)
    def __str__(self):
        return self.first_name


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("CHANNEL NAME", max_length=1000, default=None, blank=True, null=True)
    price = models.IntegerField("CHANNEL PRICE",  default=None, blank=True, null=True)
    number = models.CharField("CHANNEL NUMBER", max_length=1000, default=None, blank=True, null=True)
    def __str__(self):
        return self.name
     

class Bouquet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("BOQUET NAME", max_length=1000, default=None, blank=True, null=True)
    channels =  models.ManyToManyField( Channel, blank=True, verbose_name="ADD CHANNEL")
    price = models.IntegerField("CHANNEL PRICE",  default=None, blank=True, null=True)
    def __str__(self):
        return self.name

class Plans (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("PLAN NAME", max_length=1000, default=None, blank=True, null=True)
    bouqets = models.ManyToManyField ( Bouquet,  blank=True, verbose_name="BOQUET NAME" )
    channels = models.ManyToManyField (Channel,  blank=True,verbose_name="CHANNEL NAME" )
    price = models.IntegerField( default=None, blank=True, null=True)

    types = models.CharField("TYPE", max_length=1000, choices=TYPES,  default=None, blank=True, null=True)
    def __str__(self):
        return self.name

class Subscription (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(" NAME", max_length=1000, default=None, blank=True, null=True)
    plan = models.ForeignKey( Plans, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="PLAN NAME")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Customer Name" )
    created_at= models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name




class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supscription =  models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Subscription")
    pgid = models.CharField("PAYMENT GATEWAY ID", max_length=1000, default=None, blank=True, null=True)
    status = models.CharField("PAYMENT STATUS", max_length=1000, choices=STATUS,  default=None, blank=True, null=True)
    def __str__(self):
        return self.pgid

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_customer =  models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Customer Name", related_name="from_customer")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Name", related_name="assigned_to")
    type_ticket = models.CharField("TYPE OF TICKET", max_length=1000, choices=TICKET,  default=None, blank=True, null=True)
    message = models.URLField(max_length = 200)
    status = models.CharField("TICKET STATUS", max_length=1000, choices=STATUS,  default=None, blank=True, null=True)
    

    







    # @receiver(post_save,sender =Plans)
    # def compute(sender,instance,created, *args, **kwargs):
    #     print(instance)
    #     # print(dir(instance))
    #     # print (dir(instance.channels))
    #     # print (instance.channels.all())
    #     # print (instance.bouqets.all())
    #     bouqets_prices = list(instance.bouqets.all().values_list('price', flat=True))
    #     channels_prices = list(instance.channels.all().values_list('price', flat=True))
    #     total = sum(bouqets_prices + channels_prices)
    #     print(bouqets_prices, channels_prices, total)
    #     # import pdb 
    #     # pdb.set_trace()
    #     # instance.price = total
    #     Plans.objects.filter(id=instance.id).update(price=total)
    #     # instance.update(price=total)

@receiver(m2m_changed,sender =Plans.channels.through)
def toppings_changed(sender, instance, **kwargs):
    # print(kwargs)
    # print(instance)
    bouqets_prices = list(instance.bouqets.all().values_list('price', flat=True))
    channels_prices = list(instance.channels.all().values_list('price', flat=True))
    total = sum(bouqets_prices + channels_prices)
    # print(bouqets_prices, channels_prices, total)
    Plans.objects.filter(id=instance.id).update(price=total)

@receiver(m2m_changed,sender =Plans.bouqets.through)
def toppings_changed(sender, instance, **kwargs):
    # print(kwargs)
    # print(instance)
    bouqets_prices = list(instance.bouqets.all().values_list('price', flat=True))
    channels_prices = list(instance.channels.all().values_list('price', flat=True))
    total = sum(bouqets_prices + channels_prices)
    # print(bouqets_prices, channels_prices, total)
    Plans.objects.filter(id=instance.id).update(price=total)


# m2m_changed.connect(toppings_changed, sender=Pizza.toppings.through)