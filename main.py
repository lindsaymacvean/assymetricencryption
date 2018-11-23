import random

# See helper.py for all the variables and helper functions
from helper import *

primeOne = getFirstPrime(primes)
print('primeOne: ' + str(primeOne))

primeTwo = getFirstPrime(primes)
print('primeTwo: ' + str(primeTwo))

##      Modulus is the two primes times each other
modulus = primeOne * primeTwo
print('modulus: ' + str(modulus))

##      fn is what we use to find the ENCRYPTION EXPONENT
fn = (primeOne - 1) * (primeTwo - 1)
print('fn: ' + str(fn))

factors = findFactorsNoDupes(fn,primes)
print('factors: ' + str(factors))

##      Finding the coprime we want to use
coprimes = findCoprimes(fn,factors)
encryptionExponent = random.choice(coprimes)

publicKey = [encryptionExponent, modulus]
print('publicKey: ' + str(publicKey))

## FIND PRIVATE KEY
decryptionExponent = bruteForcePrime(encryptionExponent,fn)
privateKey = [decryptionExponent,modulus]
print('privateKey: ' + str(privateKey))

## User Interface
choice = int(input("\n\nEnter 1 for encrypting encrypt.txt \nEnter 2 for a mystery tour...\n"))

## ENCRYPTION
if choice == 1:
    with open ('encrypt.txt','r') as encrypt:
        theLines = encrypt.readlines()
        testPhrase = theLines[0]
    for character in testPhrase:
        asciiPhrase.append(asciiDict[character])
    # print('asciiPhrase: ' + str(asciiPhrase))

if choice == 'test time': ## not using this rn
    for character in testPhrase:
        asciiPhrase.append(asciiDict[character])
    # print('asciiPhrase: ' + str(asciiPhrase))

if choice == 1:
    count = 0
    for character in asciiPhrase:
        asciiPhrase[count] = str((int(asciiPhrase[count]) ** encryptionExponent) % modulus)
        count += 1
# print('asciiPhrase: ' + str(asciiPhrase))

if choice == 1:
    with open ('decrypt.txt','w+') as decrypted:
        for character in asciiPhrase:
            variable = variable + character + ' '
        decrypted.write(variable)

## DECRYPTION
if choice == 2:
    decryptionExponent = int(input('Please enter the decryption key.'))
    modulus = int(input('Please enter the modulus.'))
if choice == 2:
    with open ('decrypt.txt','r') as encrypt:
        theLines = encrypt.readlines()
        testPhrase = theLines[0]
    testPhrase = testPhrase.split(' ')
    if testPhrase[-1] == '':
        del testPhrase[-1]

if choice == 'test time123412341234': ## not using this rn
    for character in testPhrase:
        asciiPhrase.append(asciiDict[character])
    # print('asciiPhrase: ' + str(asciiPhrase))

if choice == 2:
    count = 0
    for character in testPhrase:
        testPhrase[count] = int(character)
        count += 1
    asciiPhrase = testPhrase

if choice == 2:
    count = 0
    for character in asciiPhrase:
        asciiPhrase[count] = str((character ** decryptionExponent) % modulus)
        count += 1

if choice == 2:
    decryptedPhrase = ''
    for character in asciiPhrase:
        decryptedPhrase = decryptedPhrase + asciiDecryptionDict[int(character)]
    print(decryptedPhrase)

if choice == 2:
    with open ('encrypt.txt','w+') as encrypted:
        for character in asciiPhrase:
            encrypted.write(decryptedPhrase)

if choice is 1:
    action = 'Encrypted'
elif choice is 2:
    action = 'Decrypted'
print(action + ' asciiPhrase: ' + str(asciiPhrase))

## test code below:
## factors = factors(primeMult,primes)
## print(factors)
