from secrets import *
import string

lower = 2
upper = 3

plaintext_dict = {' ': 0}
ciphertext_dict = {' ': 0}

i = 1
for letter in string.ascii_lowercase:
    plaintext_dict[letter] = i
    i += 1

i = 1
for letter in string.ascii_uppercase:
    ciphertext_dict[letter] = i
    i += 1

def keyForValue(dict, value):
    for key in dict.keys():
        if dict[key] == value:
            return key
    return

def checkIfPrime(number):
    if number == 2:
        return True
    for d in range(2, number//2 + 1):
        if number % d == 0:
            return False
    return True

def randomPrimeGenerator(lower, upper):
    n = 1
    while n < lower or n > upper:
        p = randbelow(upper)
        while checkIfPrime(p) == False or p == 1:
            p = randbelow(upper)
        q = randbelow(upper)
        while checkIfPrime(q) == False or q == 1:
            q = randbelow(upper)
        n = p * q
    return p, q, n

def eulerFunction(p, q):
    return ((p - 1) * (q - 1))

def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(a, b - a)
    if a > b:
        return gcd(a - b, b)

def randomSelection(y):
    e = randbelow(y)
    while (e == 1) or (gcd(e, y) != 1):
        e = randbelow(y)
    return e

def binaryFactorization(number):
    binaryFact = []
    number = abs(number)
    while number >= 1:
        binaryFact.append((number % 2))
        number //= 2
    return binaryFact

def repeatedSquareModularExponentiation(b, k, n):
    binaryFactorizationK = binaryFactorization(k)
    a = 1
    aux = b
    if k == 0:
        return a
    if binaryFactorizationK[0] == 1:
        a = b
    for i in range(1, len(binaryFactorizationK)):
        aux = (aux * aux) % n
        if binaryFactorizationK[i] == 1:
            a *= aux
            a = a % n
    return a

def extendedEuclideanAlgorithm(a, b):
    u2 = 1
    u1 = 0
    v2 = 0
    v1 = 1
    while b > 0:
        q = a//b
        r = a - q * b
        u = u2 - q * u1
        v = v2 - q * v1
        a = b
        b = r
        u2 = u1
        u1 = u
        v2 = v1
        v1 = v
        d = a
        u = u2
        v = v2
    return d, u, v

def generateKeys():
    p, q, n = randomPrimeGenerator((27**lower), (27**upper))
    y = eulerFunction(p, q)
    e = randomSelection(y)
    ddd, d, dd = extendedEuclideanAlgorithm(e, y)
    while d < 0:
        return generateKeys()
    return n, e, d

n, e, d = generateKeys()

def encrypt(plaintext):
    plainlist = []
    plainNumber = []
    encryptedNumber = []
    encrypted = ""
    while len(plaintext) % lower != 0:
        plaintext += " "
    for i in range(0, len(plaintext), lower):
        plainlist.append(plaintext[i:i+lower])
    for group in plainlist:
        k = lower - 1
        encode = 0
        for letter in group:
            encode = encode + ((27 ** k) * plaintext_dict[letter])
            k -= 1
        plainNumber.append(encode)
    for m in plainNumber:
        encryptedNumber.append(repeatedSquareModularExponentiation(m, e, n))
    for number in encryptedNumber:
        k = upper - 1
        for i in range(k, -1, -1):
            div = 27 ** i
            encrypted += (keyForValue(ciphertext_dict, number // div))
            number %= div
    return encrypted

def decrypt(encryptedText):
    encryptedList = []
    encryptedNumber = []
    decryptedNumber = []
    decrypted = ""
    while len(encryptedText) % upper != 0:
        encryptedText += " "
    for i in range(0, len(encryptedText), upper):
        encryptedList.append(encryptedText[i:i+upper])
    for group in encryptedList:
        k = upper - 1
        encode = 0
        for letter in group:
            encode = encode + ((27 ** k) * ciphertext_dict[letter])
            k -= 1
        encryptedNumber.append(encode)
    for c in encryptedNumber:
        decryptedNumber.append(repeatedSquareModularExponentiation(c, d, n))
    for number in decryptedNumber:
        k = lower - 1
        for i in range(k, -1, -1):
            div = 27 ** i
            decrypted += (keyForValue(plaintext_dict, number // div))
            number %= div
    return decrypted
