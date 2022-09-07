from store.models import Products

from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in self.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        product_id = str(product.id)
#        if product_id not in self.cart:
        self.cart[product_id] = {'price': float(product.price), 'quantity': int(qty)}
        self.save()

    def price_current(self, product):
        return product.price

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Products.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

# >>> from django.contrib.sessions.models import Session
# >>> s = Session.objects.get(pk='6qvuihgm0x2mftv8jbsl5r6hjdny28c3')
# s.get_decoded()
