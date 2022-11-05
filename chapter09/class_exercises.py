# 9.1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant is open")

restaurant = Restaurant('McDonalds', 'Fast Food')

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9.2 Three Restaurants

spoleto = Restaurant('Spoleto', 'Italian Food')
bobs = Restaurant('Bobs', 'Fast Food')
fogo_de_chao = Restaurant('Fogo de Chão', 'BBQ')

# spoleto.describe_restaurant()

# bobs.describe_restaurant()
# bobs.open_restaurant()

# fogo_de_chao.describe_restaurant()

# 9.3 Users
class Users:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
    
    def describe_users(self):
        """User information."""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a greeting to user"""
        print(f"\nWelcome, {self.username}!")

lain = Users('lain', 'iwakura', 'liwakura', 'lain@gmail.com', 'tokyo')
rei = Users('Rei', 'Ayanami', 'rAyanami', 'ayanamirei@gmail.com', 'tokyo-3')

# lain.describe_users()
# lain.greet_user()

# rei.describe_users()
# rei.greet_user()

# 9.4 Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served(self, value):
        self.number_served += value

    def read_served(self):
        print(f"{self.number_served} peoples served")

    def open_restaurant(self):
        print(f"The restaurant is open")

# restaurant = Restaurant("The Krusty Krab", "burger")
# restaurant.read_served()
# restaurant.set_number_served(20)
# restaurant.read_served()
# restaurant.increment_number_served(5)
# restaurant.increment_number_served(5)
# restaurant.read_served()

# 9.5
class Users:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_users(self):
        """User information."""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        """Display a greeting to user"""
        print(f"\nWelcome, {self.username}!")

lain = Users('lain', 'iwakura', 'liwakura', 'lain@gmail.com', 'tokyo')
rei = Users('Rei', 'Ayanami', 'rAyanami', 'ayanamirei@gmail.com', 'tokyo-3')

# lain.increment_login_attempts()
# lain.increment_login_attempts()
# lain.increment_login_attempts()
# lain.increment_login_attempts()
# lain.increment_login_attempts()
# print(f"login attempts: {lain.login_attempts}")

# lain.reset_login_attempts()
# print(f"login attempts: {lain.login_attempts}")

# 9.6 Ice Cream Stand 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'lemon']
    
    def display_flavors(self):
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

test = IceCreamStand('Ayy', 'Ice Cream')
# test.display_flavors()

# 9.7-8Admin
class Admin(Users):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges_admin = privileges

    def show_privileges(self):
        if self.privileges_admin:
            for privilege in self.privileges_admin:
                print(privilege, sep='')   
        else:
            print(f"This user has no privileges.")


lain_iwakura = Admin('lain', 'iwakura', 'lain369', 'lainlain@mail', 'kyoto')
# lain_iwakura.privileges.show_privileges()

# Adding privileges to admin
lain_iwakura_admin = ['can delete post', 'can ban user', 'can add post']

lain_iwakura.privileges.privileges_admin = lain_iwakura_admin
# lain_iwakura.privileges.show_privileges()

# 9.9
class Car:
    """Represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # Modifying an attribute's value through a method
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        self.battery_size = 100

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

car = EletricCar('tesla', 'model s', 2019)

car.battery.describe_battery()

car.battery.upgrade_battery()

car.battery.describe_battery()