from collections import namedtuple

# create namedtuple
Product = namedtuple('Product', ['type', 'name', 'price', 'quantity', 'id'])

# create product class
class Products:
    def __init__(self):
        self.data = []

    # add product function
    def add_product(self,type,name,price,quantity,id):
        # check id already exists or not
         for data in self.data:
            if id == data.id:
                raise ValueError (f'This {data.id} id is already exists please use another id')
         product = Product(type,name,price,quantity,id)
         self.data.append(product)

    def show_all_products(self):
          for data in self.data:
           print(f'type = {data.type} name = {data.name} price = {data.price}  quantity = {data.quantity} id = {data.id}')

    # show product's total price by id
    def show_total_price_by_id(self,id):
          for data in self.data:
           if data.id == id:
               total = data.quantity * data.price
               print(f'{data.name} products overall total = {total} ')

product = Products()
product.add_product('Electronics','headphone',50000,4,1)
product.add_product('Electronics','mouse',90000,8,2)
product.add_product('phones','redmi 7',1200000,15,3)
product.show_total_price_by_id(3)
product.show_all_products()