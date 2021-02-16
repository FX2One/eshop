
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