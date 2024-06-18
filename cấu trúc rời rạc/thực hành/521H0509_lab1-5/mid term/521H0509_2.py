import random
import math
from Crypto.Util import number

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, mod_num):
    _, x, _ = extended_gcd(a, mod_num)
    return x%mod_num

def extended_gcd(a,b):
    if(b==0): 
        return a, 1, 0
    else :
        gcd , x1 ,y1 = extended_gcd(b , a%b)
        x = y1 
        y  = x1 -(a//b)*y1  
        return gcd  , x , y

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(2, phi)
        g = gcd(e, phi)
    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(msg, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in msg]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    msg = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(msg)

if __name__ == '__main__':
    p = number.getPrime(32)
    q = number.getPrime(32)
    public_key, private_key = generate_keypair(p,q)
    print(private_key)
    print(public_key)
    print("Public Key: ", public_key)
    print("Private Key: ", private_key)
    message = "POKEMON!"
    print("Original Message: ", message)
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message: ", encrypted_message)
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message: ", decrypted_message)



