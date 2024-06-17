# creating a simple command_line or GUI based to do list application where users can add, remove, and mark tasks as completed

import time
def Add():
    n=int(input("Enter how many to-do's you want to enter: "))
    print("Loading....")
    time.sleep(2)
    for i in range(n):
        s=input("What do you want to enter ? ")
        v=input("What details do you to enter in you key? ")
        dic[s]=v
    print(dic)
def Remove():
    if(len(dic)==0):
        print("Underflow")
    elif(len(dic)!=0):
        p=input("Which key do you want to delete ? ")
        if p in dic:
            dic.pop(p)
            print(dic)
    else:
        print("Overflow")
def Mark():
    m=input("What details do you want to mark as completed ? ")
    print("Creating a new list of completed tasks \n Loading......")
    time.sleep(2)
    lst=[]
    if m in dic.values():
        lst=[m,("completed")]
        print(lst)

dic={}
print("TO ADD, PRESS '1'")
print("TO REMOVE, PRESS '2'")
print("TO MARK AS COMPLETED, PRESS '3'")
you=int(input("Enter your choice: "))
if you==1:
    Add()
elif you==2:
    Remove()
elif you==3:
    Mark()
else:
    print("WRONG CHOICE !!")