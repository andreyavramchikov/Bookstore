# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from bookstore.order.models import Order,Merchant,Delivery
from catalog.utils import COUNTRIES,STATES,PUBLISHER_TYPE_CHOICES


class Address(models.Model):
    country = models.CharField(max_length=100, choices=COUNTRIES, default=None)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=STATES, default=None)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)


    def __unicode__(self):
        return self.country + ' ' + self.city

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)


    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value by name',)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='For CEO', null=True, blank=True)
    meta_description = models.CharField(max_length=255,
                                    help_text='For CEO', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PUBLISHER_TYPE_CHOICES, default=None)

    def __unicode__(self):
        return self.name


class ActiveBookManager(models.Manager):
        def get_query_set(self):
            return super(ActiveBookManager, self).get_query_set().filter(is_active=True)

class Book(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for book page URL, created from name.',
                            null=True, blank=True)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True, default=0.00)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(verbose_name="Количество")
    description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag', null=True, blank=True)
    meta_description = models.CharField("Meta Description", max_length=255,
                                    help_text='Content for description meta tag', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    categories = models.ManyToManyField(Category, through="BookCategories")
    orders = models.ManyToManyField(Order, through='OrderBookXref')
    deliverys = models.ManyToManyField(Delivery, through='DeliveryBookXref')


    objects = models.Manager()
    active = ActiveBookManager()


    class Meta:
        ordering = ['-created_at']
        
    def __unicode__(self):
        return self.name
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_book', (), { 'book_slug': self.slug })

    def button(self):
        return '<input type="button" name="Order" value="Order" />'
    button.allow_tags = True
    button.short_description = "Action"


class BookCategories(models.Model):
    book = models.ForeignKey(Book)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.book + '_' + self.category

class OrderBookXref(models.Model):
    book = models.ForeignKey(Book)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.book.name


class DeliveryBookXref(models.Model):
    book = models.ForeignKey(Book)
    delivery = models.ForeignKey(Delivery)

    def __unicode__(self):
        return self.book.name