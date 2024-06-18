#Ex1
def thieves(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    return x

def thieves_sum(n):
    return 0 if (n<=0) else thieves(n) + thieves_sum(n - 1)
    
def isSent(day, n=40):
    return True if n - thieves_sum(day-1) - thieves(day) > 0 else False

def maxDay(n=40):
    day = 0
    while isSent(day, n):
        day += 1

    return day

#Ex2
def rishest(x):
    if len(x) == 1:
        return x[0]
    return richer(x[-1], rishest(x[0:-1]))
  
def richer(a, b):
    return max(a,b)

#Ex3
def waytochoose(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return waytochoose(n-1, k) + waytochoose(n-1, k-1)

#Ex4
def waytochooseP(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return n * waytochooseP(n-1, k-1)

#Ex5
def countCharacterAppeared(story):
    return 1 if story == 1 else 2*story + countCharacterAppeared(story-1)

#Ex6
def F(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n
    return F(n-1)+F(n-2)


#Ex7
def towerOfHanoi(A, B, C):
    def move(step, s, t, mid):
        if step > 0:
            move(step - 1, s, mid, t)

            t[1].append(s[1].pop())

            print(A)
            print(B)
            print(C)
            print('='*50)

            move(step - 1, mid, t, s)

    move(len(A[1]), A, C, B)




#ex1
print('='*100)
print("Exericises 1".upper())

thieve = 40
print("Default thieves man:", thieve)
thieve = int(input("Enter new thieve: "))
print("Ngay cuoi co the gui so linh di la", maxDay(thieve) ,'\n')

for i in range(1,  maxDay(thieve)):
    day = i
    print(
        "day",
        day,
        "ten cuop sai di",
        thieves(day),
        "sai di",
        "con lai", thieve - thieves_sum(day)
    )
    if thieve - thieves_sum(day+1) < 0:
        print(
            "day",
            day+1,
            "ten cuop sai di",
            thieve - thieves_sum(day) ,
            "sai di",
            )    

#ex2
print('='*100)
print("Exericises 2".upper())

rishestMan = [100, 101, 50, 20, 200]
print("default rishest man is", rishestMan)
isChange = input("Input c if you want to change / no: ")
if isChange == 'c':
    n = int(input("enter number of people: "))
    rishestMan = []
    for i in range(n):
        asset = float(input("enter person's money", i, ""))
        rishestMan.append(asset)
        
rishest = rishest(rishestMan)
print("first people is", rishest, "in", rishestMan)

#ex3
print('='*100)
print("Exericises 3".upper())

n = 50
way = 1000
print("default n =", n)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    n = int(input("enter new n: "))

print("default way =", way)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    way = int(input("enter new way: "))

minSub = way
k = n
i = 0
while waytochoose(n, i) < way:
    print(waytochoose(n, i))

    t_minSub = way - waytochoose(n, i)
    if t_minSub < minSub:
        minSub = t_minSub
        k = i

    i += 1

print("the", i, "that give the number of ways to choose as close to", way, "as possible.")
print("with n = ", n, "way = ", way)

# ex4
print('='*100)
print("Exericises 4".upper())


n = 50
way = 10000
print("default n=", n)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    n = int(input("enter new n: "))

print("default way=", way)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    way = int(input("enter new way: "))

i = 0
while waytochooseP(n, i) < way:
    print(waytochooseP(n, i))
    i += 1

print("the", i, "that give the number of ways to choose as close to", way, "as possible.")
print("with n = ", n, "way = ", way)

#ex5
print('='*100)
print("Exericises 5".upper())

stories = 547
print("default stories = ", stories)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    stories = int(input("enter new stories: "))
print("character appeared in", stories,
        "stories in", countCharacterAppeared(stories))

# # ex6
print('='*100)
print("Exericises 6".upper())


n = 10
print("default n = ", n)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    n = int(input("enter new n: "))

for i in range(n+2):
    print(F(i), end=" ")
print("...")
print("so fibo thu ", n, "la", F(n-1))

# ex7
print('='*100)
print("Exericises 7".upper())

n = 64
n = 3
print("default n = ", n)
isChange = input("type c if you want to change / no: ")
if isChange == 'c':
    n = int(input("enter new n: "))

A = [['A'], [i for i in range(n, 0, -1)]]
B = [['B'], []]
C = [['C'], []]
towerOfHanoi(A, B, C)
