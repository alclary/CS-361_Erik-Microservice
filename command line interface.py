print("----- WECOME TO THE JPEG TO TEXT APPLICATION! -----\n")
print(" PLEASE REVIEW THE MENU OPTIONS BELOW AND MAKE A SELECTION\n")
print("------------ MENU OPTIONS ------------")
print("     1 = LEARN ABOUT APPLICATION")
print("     2 = CONVERT JPEG to TEXT   ")
print("     3 = EXIT                   ")
print("--------------------------------------")

a = input("SELECT A NUMBER FROM THE OPTIONS ABOVE: ")


while(1):

    if int(a) == 1:
        print(
            "----------- ABOUT THIS APPLICATION ------------\n"
            "This application was developed using pytesseracts libray to covert image to text.\n"
            "It was created as a part of Oregon State Universities CS 361 class assignment.\n" 
            "The creators are Erik Blackowicz and Anthony Clary.\n")
        
        a = input("ENTER A MENU OPTION FROM ABOVE:")
        continue
        
    
    elif int(a) == 2:
        print(" \n")
        print("----------- CONVERT JPEG to TEXT ------------\n")
        in_path = input("Please enter the path to the .jpeg file you would like converted:")
        print(in_path)
        break
    
    elif int(a) == 3:
        print("THANKS FOR VISITING. GOODBYE!")
        break
        
    else:
        print("Invalid input, please review the menu options again..\n")
        a = input("SELECT A NUMBER FROM THE MENU OPTIONS ABOVE: ")
        continue
        
