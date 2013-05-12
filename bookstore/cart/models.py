# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('catalog.Product', unique=False)

    def __unicode__(self):
        return self.product.name + ' ' + str(self.quantity)

    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'Продукт в корзине'
        
    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
        
    def name(self):
        return self.product.name

    def price(self):
        return self.product.price
    
    def total(self):
        return self.quantity * self.product.price
    
    def get_absolute_url(self):
        return self.product.get_absolute_url()





    