import math

while True:
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False


    mass = input("\n    The mass of the object you are escaping (in kilograms) ")

    radius = input("\n    The distance of you and the center of the object you are escaping: (in meters) ")
 
    if not isDigit(mass):
        print("\n    Please write a number without any letters or symbols.\n")

    elif not isDigit(radius):
        print("\n    Please write a number without any letters or symbols.\n")

    else: 
        mass = float(mass)
        radius = float(radius)
        G = 0.0000000000667

        ve = math.sqrt((2*G*mass)/radius)
        ve = str(ve)
        print("\n    Your escape velocity is " + ve + " meters/second")

