class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def get_battery(self):
        return f"Battery level: {self.__battery}% 🔋"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged to {self.__battery}% ⚡")

# Derived class
class GamingPhone(Smartphone):
    def play_game(self, game):
        print(f"Playing {game} on {self.model} 🎮")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 75)
gaming_phone = GamingPhone("Asus", "ROG Phone 8", 60)

# Test methods
phone1.call("+254712345678")
print(phone1.get_battery())
phone1.charge(20)

gaming_phone.play_game("PUBG Mobile")
print(gaming_phone.get_battery())