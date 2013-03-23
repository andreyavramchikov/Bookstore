import random
from catalog.models import Product
from models import CartItem
from django.shortcuts import get_object_or_404

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]
  
def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    ''' Here depending on request I have to save to db quantity in cart and variant of it '''
    quantity = request.POST.get('quantity',1)
    product_slug = request.POST.get('product_slug','')
    product = get_object_or_404(Product, slug=product_slug)
    cart_id = _cart_id(request)
    cart_items = get_cart_items(request)
    product_in_cart = False
    for cart_item in cart_items:
        '''if alredy exist ++quantity'''
        if cart_item.product.id == product.id:
            cart_item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        cart_item = CartItem.objects.create(cart_id=cart_id, quantity=quantity, product=product)
    
    