""" A tank on the battlefield.
The code is written in the object-oriented programming paradigm.
    The control of coordinates by one dynamic object (the tank) is shown
    while trying to contact three (*) other static objects (enemies)
    according to a certain algorithm.
"""
from tank import Tank

tank = Tank()

while True:
    tank.info()
    tank.battlefield()
    if tank.battle_end():
        print("Battle over")
        break
    choice = input("management: 8 - to Straight, 6 - to Right, 2 - to Back, 4 - to Left, 5 - to Shoot, 0 - exit \n")
    match choice:
        case "8":
            tank.straight()
        case "2":
            tank.back()
        case "4":
            tank.left()
        case "6":
            tank.right()
        case "5":
            tank.shot()
        case "0":
            print("Goodbye")
            break
