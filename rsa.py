from random import randrange
from random import randint


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


def encrypt(number, publickey):
    cipher = pow(number, publickey[0], publickey[1])
    return cipher


def decrypt(cipher, privatekey):
    number = pow(cipher, privatekey[0], privatekey[1])
    return number


def createcertificate(message, privatekey):
    certificate = pow(message, privatekey[0], privatekey[1])
    return certificate


def checkcertificate(certificate, publickey):
    message = pow(certificate, publickey[0], publickey[1])
    return message
