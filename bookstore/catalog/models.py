from django.db import models

# Create your models here.
COUNTRY_CHOICES = (
    ('BR', 'Belarus'),
    ('RUS', 'Russia'),
    ('USA', 'United States'),
    ('EU', 'Europre'),
    ('OT', 'Other'),
)

STATE_CHOICES = (
    ('AL', 'Alaska'),
    ('NJ', 'New Jersey'),
)

PYBLISHER_TYPE_CHOICES = (
    ('B', 'Big'),
    ('M', 'Midium'),
    ('S', 'Small'),
)


class Address(models.Model):
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default=None)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default=None)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag', null=True, blank=True)
    meta_description = models.CharField("Meta Description", max_length=255,
                                    help_text='Content for description meta tag', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PYBLISHER_TYPE_CHOICES, default=None)

    
class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True, default=0.00)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag', null=True, blank=True)
    meta_description = models.CharField("Meta Description", max_length=255,
                                    help_text='Content for description meta tag', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    categories = models.ManyToManyField(Category, through="ProductCategories")

    class Meta:
        db_table = 'products'
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
        return ('catalog_product', (), { 'product_slug': self.slug })

class ProductCategories(models.Model):
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)