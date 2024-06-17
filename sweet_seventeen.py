""" Given a maximum of four digits to the base 17(10-> A, 11-> B, 12-> C, 16-> G) as
 input, output its decimal value.
 Input:
 23GF"""


import math
import string

def Sweet_Seventeen():
    j={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16}
    k=0
    s=0
    
    for i in m:
        if i in string.digits:
            k=int(i)

            s+=k*(int(math.pow(17,m.index(i))))
            
        elif i in j:
            
            s+=j[i]*int((math.pow(17,m.index(i))))
            
    print("Total:",s)

n=""
lst=[]
n=input("Enter a value \n (BUT 'PLEASE DO NOT ENTER 2 SIMILAR DIGITS'):")
lst=list(n)
print(lst)
m=[]
m=lst[::-1]
print(m)
Sweet_Seventeen()


"""                           COPILOT CODE

def base17_to_decimal(base17_str):
    decimal_value = 0
    base = 17
    n = len(base17_str)

    for i in range(n):
        digit = base17_str[i]
        if digit.isdigit():
            decimal_value += int(digit) * (base ** (n - i - 1))
        else:
            # Convert letters A to G to decimal values (A=10, B=11, ..., G=16)
            decimal_value += (ord(digit.upper()) - ord('A') + 10) * (base ** (n - i - 1))

    return decimal_value

# Example usage:
base17_number = "23GF"
decimal_result = base17_to_decimal(base17_number)
print(f"The decimal equivalent of {base17_number} is {decimal_result}")            """
