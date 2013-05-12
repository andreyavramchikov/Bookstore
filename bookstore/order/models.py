# -*- coding: utf-8 -*-
from django.db import models


class Order(models.Model):
    date_start = models.DateTimeField(auto_now_add=True)
    date_shipping = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Order__' + str(self.date_start)

    class Meta:
        verbose_name_plural = 'Заказ'


class Delivery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Поставка'

class Merchant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    delivery = models.ForeignKey(Delivery)

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Поставщик'