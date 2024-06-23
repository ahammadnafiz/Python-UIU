class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
    
    def update_stock(self, amount):
        self.stock += amount
    
    def apply_discount(self, percentage):
        self.price *= (1 - percentage / 100)


class ShoppingCart:
    def __init__(self):
        self.items = {}  # dictionary to hold product objects and quantities
    
    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
    
    def get_total(self):
        total = 0.0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total
    
    def create_deep_copy(self):
        new_cart = ShoppingCart()
        for product, quantity in self.items.items():
            new_cart.items[product] = quantity
        return new_cart


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.shopping_cart = ShoppingCart()
    
    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)
    
    def checkout(self):
        # Simulate order processing, e.g., creating an order object and clearing the cart
        order = Order(self, self.shopping_cart.create_deep_copy())
        # Clear the shopping cart after checkout
        self.shopping_cart = ShoppingCart()
        return order


class Order:
    def __init__(self, user, cart):
        self.user = user
        self.items = cart.items  # dictionary of product objects and quantities
        self.total_price = cart.get_total()
    
    def generate_invoice(self):
        invoice = f"Order Details for {self.user.username}:\n"
        for product, quantity in self.items.items():
            invoice += f"{product.name} - Quantity: {quantity}, Total: ${product.price * quantity:.2f}\n"
        invoice += f"Total Price: ${self.total_price:.2f}"
        return invoice


class InventoryManager:
    def __init__(self):
        self.products = []  # list to hold Product objects
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


class EcommerceSystem:
    def __init__(self):
        self.inventory_manager = InventoryManager()
        self.users = []
        self.orders = []
    
    def register_user(self, username, email):
        new_user = User(username, email)
        self.users.append(new_user)
        return new_user
    
    def process_order(self, user):
        order = user.checkout()
        self.orders.append(order)
        return order


# Create an instance of EcommerceSystem
ecommerce_system = EcommerceSystem()

# Create and add some products to the inventory
product1 = Product("Apple", 1.0, 100, "Fruits")
product2 = Product("Banana", 0.5, 150, "Fruits")
product3 = Product("Carrot", 0.75, 75, "Vegetables")

ecommerce_system.inventory_manager.add_product(product1)
ecommerce_system.inventory_manager.add_product(product2)
ecommerce_system.inventory_manager.add_product(product3)

# Register new users
user1 = ecommerce_system.register_user("user1", "user1@example.com")
user2 = ecommerce_system.register_user("user2", "user2@example.com")

# User1 adds items to their shopping cart
user1.add_to_cart(product1, 5)
user1.add_to_cart(product2, 10)

# User2 adds items to their shopping cart
user2.add_to_cart(product2, 8)
user2.add_to_cart(product3, 12)

# Process orders for both users
order1 = ecommerce_system.process_order(user1)
order2 = ecommerce_system.process_order(user2)

# Generate invoices for the orders
invoice1 = order1.generate_invoice()
invoice2 = order2.generate_invoice()

# Print invoices
print("Invoice for User 1:\n", invoice1)
print("\nInvoice for User 2:\n", invoice2)

# After processing, check the updated stock of products
print("\nUpdated Stock:")
print(f"{product1.name}: {product1.stock} units")
print(f"{product2.name}: {product2.stock} units")
print(f"{product3.name}: {product3.stock} units")
