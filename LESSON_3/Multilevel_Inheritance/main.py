print(" ~~Multilevel Inheritance~~ ")

class Device:
    def operate(self):
        return "functions smoothly"

class Smartphone(Device):
    def process(self):
        return "processes apps quickly"

class GamingPhone(Smartphone):
    def play(self):
        return f"A GamingPhone {self.operate()} and {self.process()} during gameplay."

gaming_phone = GamingPhone()
print(gaming_phone.play())
print("-" * 30)
