import random
import decimal
from django.shortcuts import get_object_or_404
from bookstore.cart.models import CartItem
from bookstore.catalog.models import Product

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
        
def update_cart(request):
    post_data = request.POST.copy()
    item_id = post_data['item_id']
    quantity = post_data['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

# remove a single item from cart
def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()
        
# gets the total cost for the current cart
def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total

    
def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))

# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    return get_cart_items(request).count()


    
    
    