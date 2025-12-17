print(" ~~Multiple Inheritance~~ ")

class Painter:
    def can_paint(self):
        return "Can paint."

class Singer:
    def can_sing(self):
        return "Can sing."

class Artist(Painter, Singer):
    def __init__(self, name):
        self.name = name
    
    def check_skills(self):
        return f"{self.name}: {self.can_paint()} {self.can_sing()}"

artist = Artist("Gab")
print(artist.check_skills())
print("-" * 30)
