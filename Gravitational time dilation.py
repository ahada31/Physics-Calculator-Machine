import math

while True:
    distance_string = input("The distance between you and the object creating the gravitational field (in meters): ")
    mass_string = input("The mass of the object creating the gravitational field (in kilograms): ")
    
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    if not isDigit(distance_string) or not isDigit(mass_string):
        print("Please write a number without any letters or symbols.")

    else:
        distance = float(distance_string)
        mass = float(mass_string)
        c_sq = 89875517873681764
        G = 0.0000000000667
        fraction_top = 2*G*mass
        fraction_bottom = distance*c_sq

        fraction = fraction_top/fraction_bottom
        inside = 1-fraction

        sqrt = math.sqrt(inside)

        gamma = 1/sqrt

        elapsedtime = 1/gamma

        print("Your time is " + elapsedtime + " slower than someone at rest.\n")