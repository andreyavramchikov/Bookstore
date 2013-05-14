# -*- coding: utf-8 -*-
from django.db import models


class Order(models.Model):
    date_start = models.DateTimeField(auto_now_add=True)
    date_shipping = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # I have to delete this fields after diplom
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return 'Order__' + str(self.date_start)

    class Meta:
        verbose_name_plural = 'Order'


class Delivery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_shipping = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_payed = models.BooleanField(default=True)
    is_delivered = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Merchant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    delivery = models.ForeignKey(Delivery)

    def __unicode__(self):
        return self.first_name
