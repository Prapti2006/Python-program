"""   
 Word is the key
 One programming language has the following keywords that cannot be used as
 identifiers:
 break, case, continue, default, defer, else, for, func, goto, if, map, range, return,
 struct, type, var
 Write a program to find if the given word is a keyword or not
 Input #1:
 defer
 Output:
 defer is a keyword
 Input #2:
 While     """

import time

def value():
    n=input("Enter a word: ")
    print("Loading.....")
    time.sleep(1)
    if n in dic.values():
        print(n," is a keyword. ")
    elif n not in dic.values():
        print(n," is not a keyword")

dic={1:"break",2:"case",3:"continue",4:"default",5:"defer",6:"else",7:"for",8:"func",9:"goto",10:"if",11:"map",12:"range",13:"return",14:"struct",15:"type",16:"var"}
value()