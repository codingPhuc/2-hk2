import math
def nextPrime(n): 
    n =n+1
    while(True):
        if checkPrime(n):
            return n 
        else : 
            n =n+1 
def checkPrime(n): 
    if(n == 2): 
        return True 
    if(n== 3):
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            return False 
    return True
def primeFact(n ): 
    arr  = list()
    for i in range(2, int(math.sqrt(n))+1):
        if checkPrime(n):
            arr.append(int(n))
            break
        if n%i == 0 and checkPrime(i) :
            n= n/i
            arr.append(i)
    return arr 
def primeFact(n): 
    arr = list()

def printPrime(n): 
    arr = list() 
    for i in range(2, n):
        if checkPrime(i):
            arr.append(i)
    s =''.join( str(arr))
    print(s)

def checkPrime(n): 
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def primeFact(n): 
    arr = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            if checkPrime(i):
                arr.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        if checkPrime(n):
            arr.append(n)
    return arr

def generate_primes(n):
    if n < 2:
        return []
    primes = [2]
    i = 3
    while i < n:
        flag = True
        for j in range(len(primes)):
            if i % primes[j] == 0:
                flag = False
                break
        if flag:
            primes.append(i)
        i += 2
    return primes

def GCD(a,b) : 
    if b == 0 or a == 0:
        return abs(a-b)
    elif a > b:
        return GCD(b, a % b) 
    else:
        return GCD(b % a, a)
    
# def LCM(a,b):
#     arr1  = primeFact(a)
#     arr2  = primeFact(b) 
#     print(arr1)
#     print(arr2)
#     dick = dict()
#     result  = []
#     # for num in arr1 : 
#     #     if num in dick : 
#     #         dick[num] +=1 
#     #     else:
#     #         dick[num] =1 
#     # for num in arr2 :
#     #     if num  in dick : 
#     #         dick[num] += 1 
#     #     else :
#     #         dick[num] = 1 
#     # for key, value in dick.items():
#     #     if value > 1:
#     #         for i in range(1,value) :
#     #             result.append(key )

def LCM(a,b): 
    return(a*b)//GCD(a,b)

def bases10_2(bas_10): 
    result = 0  ; 
    mul =1 
    while(bas_10 !=0):
        result = result + (bas_10%2)*mul
        bas_10 = bas_10//2
        mul *=10  
    return result
# def split_decimal(decimal):
#     whole_part, fractional_part = divmod(decimal, 1)
#     return int(whole_part), int(fractional_part *10**(len(str(fractional_part).split('.')[1])))
# def decimal_convertion(decimal):
#     x, y = split_decimal(decimal)
#     print('My name is {} and I am {} years old'.format(x,y))
#     print(bases10_2(x))
#     print(bases10_2(y))

def decimal_to_binary_fraction(n, num_digits):
    binary = ""
    while n != 0 and len(binary) < num_digits:
        n *= 2
        if n < 1:
            binary += "0"
        else:
            binary += "1"
            n -= 1
    return binary

def base10_to_base16(n):
    if n == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    result = ''
    while n > 0:
        remainder = n % 16
        result = hex_chars[remainder] + result
        n = n // 16
    return result
def convertbase(a, base1, base2):
    # Convert the input number a from base1 to base 10
    num = 0
    for i in range(len(a)):
        num += a[len(a)-1-i] * (base1**i)
    
    # Convert the base 10 number to base2
    res = []
    while num != 0:
        res.append(num % base2)
        num //= base2
    
    return res[::-1]
if __name__ == '__main__':
    printPrime(8)
    print(generate_primes(8))
    print(GCD(6,18))
    print(LCM(12,18))  
    print(bases10_2(6))
    print(decimal_to_binary_fraction(5.5,4))
    print(base10_to_base16(4096))