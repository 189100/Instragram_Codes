" @author: everydaycodings"
# Python Program to find sum of
# square of first n natural numbers
def squaresum(n) :
    # Iterate i from 1 and n finding
    #  square of i and add to sum.
    global sm
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
    return sm

n = 4
print(squaresum(n))

"*************************************** OUTPUT ****************************************"
# OUTPUT => 30
