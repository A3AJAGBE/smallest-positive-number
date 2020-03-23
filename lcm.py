
""" What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?  """

#import gcd from math package
from math import gcd

#define a function for the lcm
def smallest(x, y):
     return x * y // gcd(x, y) 
    
n = 1
for number in range(1, 21):
    n = smallest(n, number)
print (n)

