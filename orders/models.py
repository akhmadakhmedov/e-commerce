from enum import auto
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import AutoField
from accounts.models import Account
from store.models import Product, Variation


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    
    user            = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order_number    = models.CharField(max_length=20)
    name            = models.CharField(max_length=50)
    surname         = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=15)
    email           = models.EmailField(max_length=50, blank=True)
    payment_method  = models.CharField(max_length=10)
    address_line_1  = models.CharField(max_length=50)
    address_line_2  = models.CharField(max_length=50, blank=True)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    order_note      = models.CharField(max_length=150, blank=True)
    order_total     = models.FloatField()
    delivery_fee    = models.FloatField()
    status          = models.CharField(max_length=10, choices=STATUS, default='New')
    ip              = models.CharField(blank=True, max_length=20)
    is_ordered      = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.name} {self.surname}"

    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"

    def __str__(self):
        return self.name



