class Company:
    def __init__(self) -> None:
        self.storage = []
        self.electronicsproduct = []
        self.clothingproduct = []
        
        
    def add_items(self, item):
        self.storage.append(
            {'name':item.name, 
             'price': item.price, 
             'product_id': item.get_product_id()}
            )
    
    def add_electricproduct(self, item):
        self.electronicsproduct.append(
            {'name':item.name, 
             'price': item.price, 
             'product_id': item.get_product_id(),
             'brand':item.brand}
            )
    
    def add_clothingproduct(self, item):
        self.clothingproduct.append(
            {'name':item.name, 
             'price': item.price, 
             'product_id': item.get_product_id(),
             'type':item.type}
            )
    
    def display_products(self):
        for product in self.storage:
            print(f"{product['name']}\n{product['price']}")

class Product:
    def __init__(self, name, price, product_id) -> None:
        self.name = name
        self.price = price
        self.__product_id = product_id
        
        c.add_items(self)
    
    def get_product_id(self):
        return self.__product_id
    
    def display_info(self):
        for product in c.storage:
            print(f"{product['name']}\n{product['price']}")
    
class ElectronicsProduct(Product):
    def __init__(self, name, price, product_id, brand) -> None:
        super().__init__(name, price, product_id)
        self.brand = brand

        c.add_electricproduct(self)
    
    def display_electric_product(self):
        for product in c.electronicsproduct:
            print(f"Name: {product['name']}\nPrice: {product['price']}\nBrand: {product['brand']}")

class ClothingProduct(Product):
    def __init__(self, name, price, product_id, type) -> None:
        super().__init__(name, price, product_id)
        self.type = type

        c.add_clothingproduct(self)
    
    def display_clothing_product(self):
        for product in c.electronicsproduct:
            print(f"Name: {product['name']}\nPrice: {product['price']}\nType: {product['type']}")

class DiscountedProduct(Product):
    def __init__(self, name, price, product_id, discount_percent) -> None:
        super().__init__(name, price, product_id)
        self.discount_percent = discount_percent
    
    def calculate_discounted_price(self):
        discounted_price = self.price - (self.price * self.discount_percent / 100)
        return discounted_price

    def display_discount(self):
        super().display_info()
        print(f"Discount Percentage: {self.discount_percent}%")
        print(f"Discounted Price: ${self.calculate_discounted_price()}")
        
class Customer:
    def __init__(self, name, customer_id) -> None:
        self.name = name
        self.__customer_id = customer_id
        
        self.cart = []
    
    def get_customer_id(self):
        return self.__customer_id
    
    def add_to_cart(self,product):
        for p in self.cart:
            if p.name == product.name:
                print('Product already exists in the cart')
                return
        self.cart.append(product)
        print(f"{product.name} added to cart")
    
    def remove_from_cart(self,product):
        for p in self.cart:
            if p.name == product.name:
                self.cart.remove(p)
                print(f"{product.name} removed")
                return
        print('Product is not in the cart')
    
    def search_product(self, product):
        for p in self.cart:
            if p.name == product.name:
                c.display_products()
                return
        print('Product is not in your cart')

    def checkout(self):
        cost = []
        for item in self.cart:
            cost.append(item.price)
        
            print(f"You Purchased:\nName: {item.name}\nPrice: {item.price}")
        print(f'Total Cost: {sum(cost)}')
    


c = Company()

# Create instances of products
product1 = Product("Laptop", 1200.0, 1)
product2 = ElectronicsProduct("Smartphone", 699.99, 2, "XYZ")
product3 = ClothingProduct("T-Shirt", 19.99, 3, "Medium")
product4 = DiscountedProduct("Headphones", 99.99, 4, 15.0)

# Display information about products
c.display_products()

# Create a customer
customer = Customer("John Doe", 101)

# Add products to the customer's cart
customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)
customer.add_to_cart(product4)

# Display information about the customer's cart
customer.search_product(product2)

# Remove a product from the cart
customer.remove_from_cart(product1)

# Display information about the updated cart
customer.search_product(product2)

# Checkout and display total cost
customer.checkout()

# Display discounted product information
product4.display_discount()
