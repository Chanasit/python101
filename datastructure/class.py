class Bucket:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def updateProfile(self, name, age):
        self.name = name
        self.age = age

g = Bucket("Ong", 20)
print(g.name)
print(g.age)
g.updateProfile("Updated", 21)

print(g.name)
print(g.age)