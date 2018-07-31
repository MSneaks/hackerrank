import math
n= int(input())

for i in range(n):
    
    m = input()
    first,last = m.split()
    arr = []
    
    number_of_squares=0

    a = math.ceil(math.sqrt(int(first)))
    b = math.floor(math.sqrt(int(last)))
    print(b-a+1)
    
