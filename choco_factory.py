"""      Question #4:
 Problem Statement
A chocolate factory is packing chocolates into the packets. The chocolate packets here
 represent
an array of N number of integer values. The task is to find the empty packets(0) of chocolate
 and
 push it to the end of the conveyor belt(array).
 Example 1 :
 N=8 and arr = [4,5,0,1,9,0,5,0].
 There are 3 empty packets in the given set. These 3 empty packets represented as O should be
 pushed towards the end of the array
 Input :
 8-Value of N
 [4,5,0,1,9,0,5,0]- Element of arr[O] to arr[N-1],While input each element is separated by
 newline
 Output:
 4 5195000
 Example 2:
 Input:
 6 —Value of N.
 [6,0,1,8,0,2]- Element of arr[0] to arr[N-1], While input each element is separated by newline
 Output:
 6 18200     """

"""import time

def push():
    n=int(input("Enter how many items: "))
    for i in range(n):
        item=int(input("Enter the no. of packets: "))
        lst.append(item)
    print("Your list: ",lst)

def pop():
    if(len(lst)==0):
        print("Underflow")
    else:
        k=0
        for j in range(len(lst)):
            if(lst[j]!=0):
                lst[k]=lst[j]
            k=k+1
    print("new list: ",lst)
lst=[]
push()
pop()"""


n=int(input())
j=0
L=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        L[j]=a
        j+=1
for i in L:
    print(i,end=" ")
