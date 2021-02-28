from store.models import Product
from decimal import Decimal

'''basket class with default behaviour ,CRUD'''
class Basket():
    def __init__(self, request):
        self.session = request.session
        #creating session for first entry
        basket = self.session.get('basket_key')
        #if entry doesn't not exist, create entry with empty basket
        if 'basket_key' not in request.session:
            basket = self.session['basket_key'] = {}
        self.basket = basket

    def add(self, product, qty):
        '''add and update users basket session data'''
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': int(product.price), 'qty':int(qty)}

        '''
        saving this basket by .modified 
        '''
        self.session.modified = True

    def __iter__(self):
        '''iterate through keys in the basket'''
        product_ids = self.basket.keys()
        '''only get products flagged as active'''
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        '''
        Get the basket data and count the quantity(qty) of items
        ''''''
        iterate through the basket looking for item quantity ,when item quantity exists in the basket we add it up (sum) 
        '''
        return sum(item['qty'] for item in self.basket.values())
