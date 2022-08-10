import math
import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.ylabel('your time or length')
    plt.xlabel('time or length for someone at rest')
    plt.title('Graph of your elapsed time or length vs. someone at rest')
    plt.grid(True)
    plt.axis([0, 100, 0, 100])
    plt.plot(x,y)
    plt.show()



def inPut(thing):
    beta = thing / 100
    global length_gamma
    length_gamma = math.sqrt(1-(beta**2))
    gamma = 1 / (math.sqrt(1 - (beta**2)))
    percentage_gamma = 100 * (gamma - 1)
    percentage_length = 100 - (length_gamma * 100)

    gamma = str(gamma)
    percentage_gamma = str(percentage_gamma)
    length_gamma = str(length_gamma)
    percentage_length = str(percentage_length)

    print("\n\n     Your Gamma is " + gamma + ".\n\n")
        
        
    print("     ::TIME DILATION::\n")
    print("     your time = " + gamma + "*time at rest\n")
    print("     your elapsed time = " + length_gamma + "*elapsed time at rest\n\n\n") 

    print("     ::RELATIVISTIC MASS::\n")
    print("     M = " + gamma + "*M at rest\n")
    print("     Your mass is " + percentage_gamma + " % heavier than someone at rest or " + gamma + " times the mass for someone at rest.\n\n\n")

    print("     ::LENGTH CONTRACTION::\n")
    print("     L = " + length_gamma + "*L at rest\n")
    print("     Your length is " + percentage_length + " % smaller that someone at rest or " + length_gamma + " times the length for someone at rest.\n\n\n")

    if beta >= 0.5 and beta <= 0.9991:
        print("     In everyday electrical and electronic devices, the signals or energy travel as electromagnetic waves typically on the order of 50%–99% of the speed of light.\n")
        print("     The speed of a muon particle coming from outer space is 99.4% the speed of light.\n\n\n")
            

    elif beta <= 0.01:
        print("     A fast neutron has a speed of 0.0467% of the speed of light.\n\n\n") 

    option = input("    Would you like to enter a elapsed time? (enter 'yes' or 'no'): ")
    option = option.upper()

    if option == 'YES':
        time_string = input("\n     Enter elapsed time at rest (in seconds): ")

        if not isDigit(time_string):
            print("\n     Please write a number without any letters or symbols.")

        else:
            length_gamma = float(length_gamma)
            time = float(time_string)
                        
            elapsed_time = length_gamma*time
                        
            elapsed_time = str(elapsed_time)
            print("\n    Your elapsed time is " + elapsed_time)

    elif option == 'NO':
        pass

    else:
        print("\n     Please enter 'yes' or 'no'.")

    qgraph = input("\n      Would you like to see a graph of you vs. someone at rest? (yes or no): ")

    if qgraph == 'yes':
        def equation(x):
            global length_gamma
            length_gamma = float(length_gamma)
            return length_gamma*x
 
        graph(equation, (0, 100))

    elif qgraph == 'no':
        pass
    else:
        print("\n     Please enter 'yes' or 'no'.\n")




def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

while True:

    question = input("\n\n    Would you like to input your velocity as of meters/second or as percentage of speed of light? (enter '%' or 'm/s'): ")

    if question == '%':

        percentage_beta_string = input("\n    The percentage of the speed of light you are moving at is: ") 

        if not isDigit(percentage_beta_string):
            print("\n     Please write a number without any letters or symbols.")
    
        else:
            percentage_beta = float(percentage_beta_string)

            if percentage_beta == 100:
                print("\n     Your Gamma is infinity.\n\n")

                print("     ::TIME DILATION::\n")
                print("     t = infinity*t at rest\n")
                print("     your elapsed time = 0\n")
                print("     Your time is infinity times slower than someone at rest.\n\n")

                print("     ::RELATIVISTIC MASS::\n")
                print("     Your mass is infinity.\n\n")

                print("     ::LENGTH CONTRACTION::\n")
                print("     Your length is 0.\n")

            elif percentage_beta == 0:
                print("\n     Your Gamma is 1.\n")
                print("     You are at rest.\n\n")

            elif percentage_beta > 100:
                print("\n     Sorry, you cannot travel faster than the speed of light.\n\n")

            elif percentage_beta < 0:
                print("\n     Please enter a positive number.\n\n")
            else: 
                inPut(percentage_beta)


                

    elif question == 'm/s':
        meter_second_string = input("\n     Enter your velocity in meter per second: ")

        if not isDigit(meter_second_string):
            print("\n     Please enter a number without any letters or symbols.")

        else:
            meter_second = float(meter_second_string)

            betam = meter_second / 299792458

            if betam == 1:
                print("\n     Your Gamma is infinity.\n\n")

                print("     ::TIME DILATION::\n")
                print("     t = infinity*t at rest\n")
                print("     your elapsed time = 0\n")
                print("     Your time is infinity times slower than someone at rest.\n\n")

                print("     ::RELATIVISTIC MASS::\n")
                print("     Your mass is infinity.\n\n")

                print("     ::LENGTH CONTRACTION::\n")
                print("     Your length is 0.\n")

            elif betam == 0:
                print("\n     Your Gamma is 1.\n")
                print("     You are at rest.\n\n")
            
            elif betam > 1:
                print("\n     Sorry, you cannot travel faster than the speed of light.\n\n")
            
            elif betam < 0:
                print("\n     Please enter a positive number.\n\n")
            
            else:
                percentage_betam = betam*100
                inPut(percentage_betam)
                

    else:
        print("\n\n     Please enter 'm/s' or '%'.")