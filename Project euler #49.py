import time
import math
start = time.time()
primelist= []

def permutationchecker(prime1,prime2,prime3):
    permutationlist = set(list(prime1)+list(prime2)+list(prime3))
    if len(permutationlist) <= 4:
        if int(prime1) != 1487:
            end = time.time()
            print(prime1+prime2+prime3)
            print(end - start)
            exit()

def primechecker2(number):
    for x in range(3, int(math.sqrt(number + 1)), 2):
        if number % x == 0:
            return None
    permutationchecker(str(number-6660),str(number-3330),str(number))

def primechecker(number):
    for x in range(3,int(math.sqrt(number+1)),2):
        if number % x == 0:
            return None
    primechecker2(number+3330)

def primefinder(number):
    prime = [True] * (number+1)
    for y in range(3,int(math.sqrt(number)+1),2):
        if prime[y] == True:
            for x in range(y**2, number + 1,y+y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if x > 1000:
            if prime[x] == True:
                primelist.append(x)

primefinder(10000-6660)

for x in primelist:
    primechecker(x+3330)
