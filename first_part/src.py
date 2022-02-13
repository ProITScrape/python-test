
import operator
import functools

def exercise_one():
    # Python Program to print:
        # For every multiple of 3 print "Three".
        # For every multiple of 5 print "Five".
        # And for every multiple of both 3 and 5 print "ThreeFive"

    # Loop for 100 times
    for number in range(1,100):
        # number divisible by 5 and 3 : 5*3=15, X%15 ==0 or X%5==0 and X%3==0
        if number%15 == 0:		
            print("ThreeFive")
            continue
        #number divisible by 3 X%3==0 ==> print "Three".
        elif number % 3 == 0:
            print("Three")
            continue
        #number divisible by 5 X%5==0 ==> print "Five".
        elif number % 5 == 0:
            print("Five")
            continue
        print(number)


def  exercise_two(number):
        l = [int(x) for x in str(number)]
        k = []
        for i,x in enumerate(l):
            if i<len(l)-1:
                r=[x,l[i+1]]
                product = functools.reduce(operator.mul,r)
                k.append(product)  
        k.append(functools.reduce(operator.mul,l))    
        result = l+k
        if len(set(result)) != len(result):
            return False
        return True
            

# exercise 3
def calculate(l):
    if isinstance(l, list):
        return  sum([int(i) for i in l if type(i)== str  and  i.isdigit()])
    return False


## exercise 4
def anagrams(word,array):
    anagrams = []
    letters = [letter for letter in word]
    letters.sort()
    for value in  array:
        x = [letter for letter in value]
        x.sort()
        if x == letters:
            anagrams.append(value)
    return anagrams
    

