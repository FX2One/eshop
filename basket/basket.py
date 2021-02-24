
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
