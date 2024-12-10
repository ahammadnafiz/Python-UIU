class Vehicle:
    def __init__(self, vehicle_type, rate) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
    
    def calculate_rent(self, duration):
        return self.rate * duration

class Insurence:
    def __init__(self, insurance_type, cost_per_day) -> None:
        self.insurance_type = insurance_type
        self.cost = cost_per_day
    
    def calculate_rent(self, duration):
        return self.cost * duration

class Rental:
    def __init__(self, vehicle, duration) -> None:
        self.vehicle = vehicle
        self.duration = duration
        self.total_price = 0
    
    def total_cost(self, insurance = None):
        vehicle_cost = self.vehicle.calculate_rent(self.duration)
        insurance_cost = 0
        
        if insurance:
            insurance_cost = insurance.calculate_rent(self.duration)
        
        self.total_price = vehicle_cost + insurance_cost
        return self.total_price

class Customer:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.rentals = []
        self.total_cost = 0
    
    def create_rental(self, vehicle_type, duration, insurance_type = None):
        vehicle = self._create_vehicle(vehicle_type)
        rental = Rental(vehicle, duration)
        
        if insurance_type:
            insurance = self._create_insurance(insurance_type)
            self.total_cost = rental.total_cost(insurance)
        else:
            self.total_cost = rental.total_cost()

        self.rentals.append(rental)
        return self.total_cost
        
    def _create_vehicle(self, vehicle_type):
        if vehicle_type == 'Economy':
            return Vehicle('Economy', 300)
        elif vehicle_type == 'Standard':
            return Vehicle('Standard', 500)
        elif vehicle_type == 'Luxury':
            return Vehicle('Luxury', 1000)
    def _create_insurance(self, insurance_type):
        if insurance_type == "Basic":
            return Insurence("Basic", 200)
        elif insurance_type == "Premium":
            return Insurence("Premium", 300)
        

# Example usage:

# Create a customer
customer1 = Customer("Alice Smith", "456 Oak St")

# Rent an Economy vehicle for 3 days with Basic insurance
total_cost1 = customer1.create_rental("Economy", 3, "Basic")
print(f"Total rental cost: {total_cost1} BDT")

# Create another customer
customer2 = Customer("Bob Johnson", "789 Pine St")

# Rent a Luxury vehicle for 7 days without insurance
total_cost2 = customer2.create_rental("Luxury", 7)
print(f"Total rental cost: {total_cost2} BDT")

# Create another customer
customer3 = Customer("Eva Brown", "101 Elm St")

# Rent a Standard vehicle for 5 days with Premium insurance
total_cost3 = customer3.create_rental("Standard", 5, "Premium")
print(f"Total rental cost: {total_cost3} BDT")
