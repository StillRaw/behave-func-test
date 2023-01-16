import math
import os

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def input_numbers(num1,num2):
    # Entering values by keyboard
    num1_numeric=False
    num2_numeric=False

    # Check values are float or other type.
    # num1 is not numeric scenario.
   
    if not isfloat(num1):
        num2=num1
    else:
        num1_numeric=True

    # num2 is not numeric scenario.
    if num1.isnumeric():
        
        if not isfloat(num2):
            num1=num2
        else:
            num2_numeric=True

    # Make final decision about values.   
    if (num1_numeric is False) or (num2_numeric is False):
        return 'Values must be numeric!'
    else:
        return num1,num2
    
def odd_numbers(num1,num2):
    
    # Transform string input to float number.
    num1=float(num1)
    num2=float(num2)

    # To indentify interval and make sequence is unimportant.
    if num2 < num1:
        num1,num2 = num2,num1
    elif num2 == num1:
        if num1 % 2 == 0:
            odd_number_list=["No value found in given interval."]
            print("No odd numbers found. Because, values are same and these are even number.")
            return odd_number_list
    
    # To make clear float numbers by the terms of its sign(negative or positive).
    if num1 >= 0 and num2>= 0:
        num1=math.ceil(num1)
        num2=math.floor(num2)
    elif num1 < 0 and num2 >= 0:
        num1=math.ceil(num1)
        num2=math.floor(num2)
    elif num1 >= 0 and num2 < 0:
        num1=math.floor(num1)
        num2=math.ceil(num2)
    elif num1 < 0 and num2 < 0:
        num1=math.ceil(num1)
        num2=math.floor(num2)

    odd_number_list=[i for i in range(num1,num2+1)   if i % 2 == 1]
    odd_number_list.sort()

    print(odd_number_list)
    
    return odd_number_list

if __name__=='__main__':
    num1 = input("Enter the first value:")
    num2 = input("Enter the second value:")
    input_numbers(num1,num2)
    if input_numbers(num1,num2) == 'Values must be numeric!':
        os._exit(100)
    odd_numbers(num1,num2)