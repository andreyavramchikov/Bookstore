# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    book = models.ForeignKey('catalog.Book', unique=False)

    def __unicode__(self):
        return self.book.name + ' ' + str(self.quantity)

    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'Book in cart'
        
    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
        
    def name(self):
        return self.book.name

    def price(self):
        return self.book.price
    
    def total(self):
        return self.quantity * self.book.price
    
    def get_absolute_url(self):
        return self.book.get_absolute_url()





    