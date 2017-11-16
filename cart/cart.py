import datetime
from cart import models

CART_ID = 'CART-ID'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, produit, unit_price, quantity=1):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                produit=produit,
            )
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.produit = produit
            item.unit_price = unit_price
            item.quantity = quantity
            item.save()
            self.cart.total = self.summary()
            self.cart.save()
        else: #ItemAlreadyExists
            item.unit_price = unit_price
            item.quantity += int(quantity)
            item.save()
            self.cart.total = self.summary()
            self.cart.save()




    def remove(self, produit):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                produit=produit,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()
            self.cart.total = self.summary()
            self.cart.save()

    def update(self, produit, quantity, unit_price=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                produit=produit,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else: #ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
                item.save()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result
        
    def summary(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_price
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
        self.cart.total = self.summary()
        self.cart.save()

