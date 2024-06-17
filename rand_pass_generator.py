import random
import string
n=int(input("Enter the length of the password : "))
char_values=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
password=""

for i in range(n):
    password += random.choice(char_values)
print("YOUR RANDOM GENERATED PASSWORD IS: \n ",password)