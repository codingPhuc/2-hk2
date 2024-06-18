P = "You get good grade in the midterm exam"
Q = "You understand how to solve all the exercises in the book"

# Statement (a)
statement_a = "If you understand how to solve all the exercises in the book, then you will get a good grade in the midterm exam, and if you get a good grade in the midterm exam, then you understand how to solve all the exercises in the book."
print(statement_a)

# Statement (b)
statement_b = "You understand how to solve all the exercises in the book, but you did not get a good grade in the midterm exam."
print(statement_b)

# Statement (c)
statement_c = "Understanding how to solve all the exercises in the book implies that you will get a good grade in the midterm exam."
print(statement_c)

#ex2 
def if_then(a,b):
    return " if "+ a+ ",then "+b
def If(a,b):
    return a+  " if " +b 
def Only_if(a,b):
    return  a+  " if and only if " +b 
print(if_then(Q ,P) + if_then(P,Q) )
print()
print(If(P,Q))
print()
print(Only_if(Q,P))
print()

#ex3 
print("contrapositive is")
print("if You did't understand how to solve all the exercises in the , then you wont get good grade ")
print("if you did't get good grade , then you did't understand all the exercises in the book")
print("you  understand all the exercises in the book   , then you get good grade")


#ex4 
p = "Phong has Visa"
q = "Phong can fly"
r = "Phong can speak English"
t = "Phong goes to America"

# Premises
premise1 = p
premise2 = "If " + q + ", " + t
premise3 = "If " + r + ", " + t

# Conclusion
conclusion = t

p = "An wakes up late"
q = "The traffic is flowing smooth"
not_q = "The traffic is heavy"
r = "School day"
s = "An has to go to school"
v = "An is late for school"
p = True  # An wakes up late
q = True  # The traffic is flowing smooth
not_q = False  # The traffic is heavy
r = True  # School day
s = True  # An has to go to school
v = True  # An is late for school
def implies(p, q):
    """Returns the truth value of the implication p -> q."""
    return not p or q
# Premises
premise1 = r and not q
premise2 = implies(p,v)
premise3 = implies(r,s)
premise4 =  implies(not r, not v)

# Conclusion
conclusion = v

import math

A=[
[2 ,0 ,5 ,0 ,3 ,0],
[3 ,0 ,0 ,0 ,0 ,0],
[0 ,6 ,2 ,0 ,5 ,0],
[3 ,0 ,9 ,0 ,25 ,0],
[0 ,0 ,2 ,4 ,5 ,0],
[0 ,0 ,0 ,0 ,0 ,5]
]
def isOdd(a):
    return a % 2 != 0

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

def isSquare(a):
    return math.isqrt(a)**2 == a

def isGreater(a, b):
    return a > b

def isEqual(a, b):
    return a == b

def isAbove(a, b):
    return a[0] < b[0]

def isLeftOf(a, b):
    return a[1] < b[1]

def check_statement():
    for row in A:
        for elem in row:
            if not isOdd(elem) and isPrime(elem):
                return True
    return False

def check_statement():
    for row in A:
        for elem in row:
            if isOdd(elem) and not isSquare(elem):
                return False
    return True


def check_statement_c():
    for row in A:
        for elem in row:
            if isOdd(elem) and not isGreater(elem, 2):
                return False
    return True

def check_statement_d():
    for row in A:
        for elem in row:
            if isPrime(elem) and (isGreater(elem, 3) or isEqual(elem, 3)):
                return False
    return True

def check_statement_e():
    for row_a, row in enumerate(A):
        for col_a, elem_a in enumerate(row):
            for col_b in range(col_a + 1, len(row)):
                if isLeftOf((row_a, col_a), (row_a, col_b)):
                    continue
                if isLeftOf((row_a, col_b), (row_a, col_a)):
                    continue
                if isLeftOf((row_a, col_a), (row_a, col_b)):
                    return False
    return True

import math

def isOdd(a):
    return a % 2 == 1

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

def isSquare(a):
    return math.sqrt(a).is_integer()

def isGreater(a, b):
    return a > b

def isEqual(a, b):
    return a == b

def isAbove(a, b):
    return a[0] < b[0]

def isLeftOf(a, b):
    return a[1] < b[1]


