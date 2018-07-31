import math

T = int( input() )
for t in range(T):
    A, B = [ int(v) for v in input().split() ]
    ar = math.ceil( math.sqrt(A) )
    br = math.floor( math.sqrt(B) )
    print( br-ar+1 )
