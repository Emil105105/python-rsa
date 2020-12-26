#!requires python3.8 or later!
#
#sorry for my bad English
#if you don't want to import 'random' from the standard library, you can replace 'randint' and 'randrange' with your own functions
from random import randrange
from random import randint

#this is just to show how fast the algorithm is
#remove this in your projects
from time import time
starttime = time()

#the rabin miller primality test algorithm isn't a 100% correct algorithm for checking if a number is prime
#if you want a 100% correct algorithm, use the function 'isprime' and fill out the essential fields
#thanks to https://gist.github.com/Ayrx for a python implementation
def ismillerprime(n, k):
    if n == 1:
        return False
    if n in [2, 3, 5, 7, 11, 13, 17, 19]:
        return True
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        if n % p == 0:
            return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# you can delete this part if you want to use the faster rabin miller primality test
# 
# def isprime(n):
#     if n == 1:
#         return False
#     if n in [2, 3, 5, 7]:
#         return True
#     s = n ** 0.5 #you can use import math and math.sqrt(n) here
#     for p in [#put here the list of prime numbers up to 10 ** (rsanlength / 4 + 1)]:
#         if p > s:
#             break
#         if n % p == 0:
#             return False
#     return True
# 


def randomprime(length, millerrounds):
    length -= 1
    start = randint(10 ** length, 10 ** length * 9)
    if start % 2 == 0:
        start += 1
    counter = 0
    isloop = True
    while isloop:
        testnumber = start + (counter * 2)
        if ismillerprime(testnumber, millerrounds):
            isloop = False
        counter += 1
    return testnumber

    
def generatekeys(length, millerrounds):
    p = randomprime(length // 2, millerrounds)
    q = randomprime(length // 2, millerrounds)
    while p == q:
        q = randomprime(length // 2, millerrounds)
    n = p * q
    phin = (p - 1) * (q - 1)
    e = randomprime(length // 2, millerrounds)
    while phin % e == 0 or n % e == 0:
        e = randomprime(length // 2, millerrounds)
    d = pow(e, -1, phin)
    del p
    del q
    return [[e, n], [d, n]]

#please notice that only integers (or text/binary data that was convertet to an integer) can be encrypted
def encrypt(number, publickey):
    cipher = pow(number, publickey[0], publickey[1])
    return cipher


def decrypt(cipher, privatekey):
    number = pow(cipher, privatekey[0], privatekey[1])
    return number

#please notice that only integers (or text/binary data that was convertet to an integer) can be used to create a signature
#I recommend to use the hash of the message instead
def createsignature(message, privatekey):
    signature = pow(message, privatekey[0], privatekey[1])
    return signature


def checksignature(signature, publickey):
    message = pow(signature, publickey[0], publickey[1])
    return message


if __name__ == '__main__':
    #this is an example. Delete this part in your project
    #the recommended number of rounds for the rabin miller prime test is 64 and the optimal number of rounds is 40
    #the larger the number, the smaller the probability that a number is incorrectly recognized as a prime
    millerrouds = 64
    #this is the number of base 10 digits of the mod number(N or n) of the RSA algorithm
    #for secure encryption this number should be higher than 300
    rsanlength = 320
    keys = generatekeys(rsanlength, millerrouds)
    publickeys = keys[0]
    privatekeys = keys[1]
    message = randint(10 ** 4, 10 ** 8)
    encrypted = encrypt(message, publickeys)
    decrypted = decrypt(encrypted, privatekeys)
    signature = createsignature(message, privatekeys)
    checked = checksignature(signature, publickeys)
    timeneeded = time() - starttime
    print('\nPublickeys:')
    print(publickeys[0])
    print()
    print(publickeys[1])
    print('\nPrivatekeys:')
    print(privatekeys[0])
    print()
    print(privatekeys[1])
    print('\nMessage:')
    print(message)
    print('\nEncrypted:')
    print(encrypted)
    print('\nDecrypted:')
    print(decrypted)
    print('\nSignature:')
    print(signature)
    print('\nChecked signature:')
    print(checked)
    print('\nTime needed:')
    print(timeneeded)
    