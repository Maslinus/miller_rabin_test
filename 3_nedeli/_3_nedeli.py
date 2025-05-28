from os import read
from tkinter import W
import numpy as np
import random

#Miller_Radin_test
        
def My_Pow(number, power, mod):
    if (power == 0):
        return 1;
    if (power == 1):
        return number % mod

    t = My_Pow(number, int(power / 2),mod)
    t = (t * t) % mod

    if (power % 2 == 0):
        return t
    else:
        return ((number % mod) * t) % mod
        
def miller_rabin(n, k = -1):
    if k == -1:
        k = int(np.log(n))
    if n == 2:
        print(n,k, " - prime number\n")
        result.write(str(n)+" "+ str(k) + " - prime number\n")
        return True

    if n % 2 == 0:
        print(n,k, " - composite number\n")
        result.write(str(n)+" "+ str(k) + " - prime number\n")
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = My_Pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = My_Pow(x, 2, n)
            if x == n - 1:
                break
        else:
            print(n,k, " - composite number\n")
            result.write(str(n)+" "+ str(k) + " - prime number\n")
            return False
    print(n,k, " - prime number\n")
    result.write(str(n)+" "+ str(k) + " - prime number\n")
    return True

def Parse(str_num):
    num_list = str_num.split()
    int_list = []
    for num in num_list:
        int_list.append(int(num))
    return int_list


Flag = True
while Flag == True:
    result = open("Result.txt", "w")
    print("Enter 1 to manually enter a number\nEnter 2 to enter a number from a file\nto stop work, enter 3\n")
    a = int(input())
    if(a == 1):
        print("Enter a number or numbers:\n")
        n = Parse(input())
        print("Enter the number of rounds manually - enter: 1\nThe number of rounds is equal log(number) - enter: 2\n")
        b = int(input())
        for i in range(0,len(n)):
            if(b == 1):
                print("Enter the number of rounds for the number ",n[i],":\n")
                miller_rabin(n[i],int(input()))
            if(b == 2):
                miller_rabin(n[i])
            
    if(a == 2):
        print("Enter the file name (example: file_with_numbers.txt):\n")
        File = open(input(),"r")
        Text = File.readlines()
        n = []
        for line in Text:
            nums_in_line = [int(num) for num in line.strip().split()]
            n.append(nums_in_line)
        for i in range(0, len(n)):
            if(len(n[i])>1):
                miller_rabin(n[i][0],n[i][1])
            else:
                miller_rabin(n[i][0])
    print("Solution saved to file: Result.txt\n")
                
    if(a == 3):
        Flag = False
