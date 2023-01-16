import math

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def input_numbers():
    # Entering values by keyboard
    num1_numeric=False
    num2_numeric=False

    # Check values are float or other type.
    num1 = input("Enter the first value:")
    while num1_numeric==False:
        if not isfloat(num1):
            num1 = input("First value must be numeric value:")
        else:
            num1_numeric=True

    num2 = input("Enter the second value:")
    while num2_numeric==False:
        if not isfloat(num2):
            num2 = input("Second value must be numeric value:")
        else:
            num2_numeric=True
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
    num1,num2=input_numbers()
    odd_numbers(num1,num2)