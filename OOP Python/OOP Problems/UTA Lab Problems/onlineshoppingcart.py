import copy

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        self.stock += amount
        print(f"Updated stock for {self.name}: {self.stock}")

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Updated quantity for {self.product.name}: {self.quantity}")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.name == product.name:
                item.update_quantity(item.quantity + quantity)
                return
        self.items.append(CartItem(product, quantity))
        print(f"Added {quantity} {product.name}(s) to cart")

    def remove_item(self, product):
        self.items = [item for item in self.items if item.product.name != product.name]
        print(f"Removed {product.name} from cart")

    def update_item_quantity(self, product, new_quantity):
        for item in self.items:
            if item.product.name == product.name:
                item.update_quantity(new_quantity)
                return
        print(f"{product.name} not found in cart")

    def get_total(self):
        return sum(item.product.price * item.quantity for item in self.items)

    def deep_copy(self):
        return copy.deepcopy(self)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product):
        self.cart.remove_item(product)

    def checkout(self):
        total = self.cart.get_total()
        print(f"Checkout completed. Total: ${total:.2f}")
        self.cart = ShoppingCart()  # Clear the cart after checkout

# Demonstration
if __name__ == "__main__":
    # Create products
    apple = Product("Apple", 0.5, 100)
    banana = Product("Banana", 0.3, 150)
    orange = Product("Orange", 0.6, 80)

    # Create a customer
    customer = Customer("John Doe", "john@example.com")

    # Add products to the cart
    customer.add_to_cart(apple, 5)
    customer.add_to_cart(banana, 3)
    customer.add_to_cart(orange, 2)

    # Update quantities
    customer.cart.update_item_quantity(apple, 7)
    customer.cart.update_item_quantity(banana, 4)

    # Remove an item from the cart
    customer.remove_from_cart(orange)

    # Create a deep copy of the cart
    cart_copy = customer.cart.deep_copy()

    # Modify the original cart
    customer.add_to_cart(orange, 1)
    customer.cart.update_item_quantity(apple, 10)

    # Show that modifying the original cart doesn't affect the copy
    print("\nOriginal Cart:")
    for item in customer.cart.items:
        print(f"{item.product.name}: {item.quantity}")
    print(f"Total: ${customer.cart.get_total():.2f}")

    print("\nCopied Cart:")
    for item in cart_copy.items:
        print(f"{item.product.name}: {item.quantity}")
    print(f"Total: ${cart_copy.get_total():.2f}")

    # Checkout
    customer.checkout()