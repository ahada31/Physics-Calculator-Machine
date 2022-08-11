import math

speed_of_sound = 331.0

def source_towards(frequency, velocity):
    step1 = speed_of_sound - velocity
    step2 = speed_of_sound / step1
    final_frequency = step2 * frequency
    final_frequency = str(final_frequency)
    print("\n       The observer will experience a frequency of " + final_frequency + " Hz when the source moves towards it.")

def source_away(frequency, velocity):
    step1 = speed_of_sound + velocity
    step2 = speed_of_sound / step1
    final_frequency = step2 * frequency
    final_frequency = str(final_frequency)
    print("\n       The observer will experience a frequency of " + final_frequency + " Hz when the source moves away from it.")


def observer_towards(frequency, velocity):
    step1 = speed_of_sound + velocity
    step2 = step1 / speed_of_sound
    final_frequency = step2 * frequency
    final_frequency = str(final_frequency)
    print("\n       The observer will experience a frequency of " + final_frequency + " Hz when the observer moves towards the source.")

def observer_away(frequency, velocity):
    step1 = speed_of_sound - velocity
    step2 = step1 / speed_of_sound
    final_frequency = step2 * frequency
    final_frequency = str(final_frequency)
    print("\n       The observer will experience a frequency of " + final_frequency + " Hz when the observer moves away from the source.")


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

while True:

    relative_position = input("\n\n       In this scenario, is there a moving source or a moving observer (type 'source' or 'observer')?\n\n ")

    if relative_position == 'source':
        approach = input("\n       Is the source moving towards the observer or away from the observer (type 'towards' or 'away')?\n ")
        if approach == 'towards':

            frequency_source_string = input("\n       What is the frequency (in Hz) of the moving source?\n ")

            velocity_source_string = input("\n       What is the velocity (in m/s) of the moving source?\n ")
            
            if not isDigit(frequency_source_string):
                print("\n       Please input a number.\n")

            elif not isDigit(velocity_source_string):
                print("\n       Please input a number.\n")

            else:
                frequency_source = float(frequency_source_string)
                velocity_source = float(velocity_source_string)
                source_towards(frequency_source, velocity_source)

        elif approach == 'away':

            frequency_source_string = input("\n       What is the frequency (in Hz) of the moving source?\n ")

            velocity_source_string = input("\n       What is the velocity (in m/s) of the moving source?\n ")

            if not isDigit(frequency_source_string):
                print("\n       Please input a number.\n")

            if not isDigit(velocity_source_string):
                print("\n       Please input a number.\n")

            else:
                frequency_source = float(frequency_source_string)
                velocity_source = float(velocity_source_string)
                source_away(frequency_source, velocity_source)
     
        else:
            print("\n       Please input 'towards' or 'away'.\n")      

    elif relative_position == 'observer':
        approach = input("\n       Is the observer moving towards the source or away from the source (type 'towards' or 'away')?\n ")
        if approach == 'towards':

            frequency_source_string = input("\n       What is the frequency (in Hz) of the moving observer?\n ")

            velocity_source_string = input("\n       What is the velocity (in m/s) of the moving observer?\n ")
            
            if not isDigit(frequency_source_string):
                print("\n       Please input a number.\n")

            elif not isDigit(velocity_source_string):
                print("\n       Please input a number.\n")

            else:
                frequency_source = float(frequency_source_string)
                velocity_source = float(velocity_source_string)
                observer_towards(frequency_source, velocity_source)

        elif approach == 'away':

            frequency_source_string = input("\n       What is the frequency (in Hz) of the moving observer?\n ")

            velocity_source_string = input("\n       What is the velocity (in m/s) of the moving observer?\n ")

            if not isDigit(frequency_source_string):
                print("\n       Please input a number.\n")

            if not isDigit(velocity_source_string):
                print("\n       Please input a number.\n")

            else:
                frequency_source = float(frequency_source_string)
                velocity_source = float(velocity_source_string)
                observer_away(frequency_source, velocity_source)
     
        else:
            print("\n       Please input 'towards' or 'away'.\n")   
        
    else:
        print("\n       That is neither a moving source or observer. Please try again.\n")  