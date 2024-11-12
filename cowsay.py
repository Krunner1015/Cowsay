import sys
from heifer_generator import *

def list_cows(cows):
    available_cows = ""

    for cow in cows:
        available_cows += cow.get_name() + " "

    return available_cows

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():
    cows = get_cows()

    if sys.argv[1] == "-l":
        available_cows = list_cows(cows)
        print(f"Cows available: {available_cows}")

    elif sys.argv[1] == "-n":
        cow_name = sys.argv[2]
        cow = find_cow(cow_name, cows)

        if cow:
            print(" ".join(sys.argv[3:]))
            print(cow.get_image())

            if isinstance(cow, Dragon):
                if cow.can_breath_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
        else:
            print(f"Could not find {cow_name} cow!")
    else:
        cow_name = cows[0].get_name() #this is the default cow
        cow = find_cow(cow_name, cows)
        print(" ".join(sys.argv[1:]))
        print(cow.get_image())

if __name__ == '__main__':
    main()