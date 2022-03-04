# Ryan Lugo: RJL 3/4/22


def build_car(wheels,axels,doors,color):
    return "The car has",wheels,"Wheels",axels,"Axels",doors,"Doors","And is",color

wheel = input("Wheels: ")
axel = input("Axels: ")
door = input("Doors: ")
color = input("Color: ")

print(build_car(wheel,axel,door,color))