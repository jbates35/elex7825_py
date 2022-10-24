import robot as rob
import camera as cam

import cv2, PIL, os



#ALL LAB CODE GOES HERE:...
def lab1():
    pass

def lab2():
    pass

def lab3():
    _robot = rob.Robot()
    

def lab4():
    pass

def lab5():
    pass

def lab6():
    pass

def lab7():
    pass


#Switch lab based on input
def select_lab(lab):
    if int(lab) == 1: lab1()
    elif int(lab) == 2: lab2()
    elif int(lab) == 3: lab3()
    elif int(lab) == 4: lab4()
    elif int(lab) == 5: lab5()
    elif int(lab) == 6: lab6()
    elif int(lab) == 7: lab7()
    else: print("Error...")
    
    
if __name__ == "__main__":
    
    exit = False # turns true when q is pressed

    while exit==False:
        
        #read lab intro
        with open('intro.txt') as f:
            print(f.read())
            
        #get user input and select first char
        x = input("Select lab: \n")
        x = x[0]

        #Select lab, or exit if q is pressed
        if x[0].isnumeric():
            select_lab(x[0])
        elif x[0] == 'q' or x[0] == 'Q':
            exit = True
        else:
            print("Incorrect input")           

