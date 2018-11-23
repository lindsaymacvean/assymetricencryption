import random

primeMult = 189027348
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,89,97,101,103,107,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
factors = []
asciiDict = {
    }
imprtNum = -1
modulus = 0
result = 0
primeOne = 0
primeTwo = 0
fn = 0
encryptionExponent = 0
coprimes = []
publicKey = []
decryptionExponent = 0
privateKey = []
asciiPhrase = []
testPhrase = "This is a secret message"
variable = ''

## IMPORTS THE PRIME LIST
with open('primes.txt','r') as primeDoc:
    primeList = primeDoc.readlines()
    primeString = primeList[0]
    primes = primeString.split(',')
    for number in primes:
        primes[result] = int(primes[result])
        result += 1

## IMPORT THE ASCII DICTIONARY
with open ('asciifixed.txt','r') as asci:
    imprt = asci.readlines()
    print(imprt)
    for item in imprt:
        toEditNum = -2
        imprtNum += 1
        if imprtNum == 0:
            imprtNum += 1
        elif imprtNum == len(imprt):
            break
        toEdit = imprt[imprtNum]
        toEdit = toEdit[:-1]
        if ':135' in toEdit:
            asciiDict[toEdit[0:1]] = int(toEdit[3:])
        else:
            asciiDict[toEdit[0]] = int(toEdit[2:])
    asciiDict[' '] = 66
    print(asciiDict)

## SETTUPING UP DECRYPTION DICTIONARY
asciiDecryptionDict = {
    }
for item in asciiDict:
    asciiDecryptionDict[asciiDict[item]] = item
print(asciiDecryptionDict)


## FINDS FACTORS GIVEN A NUMBER
def findFactors(num, primeList):
    factorList = []
    for number in primeList:
        if num % int(number) == 0:
            factorList.append(int(number))
            checkAgain(int(number),num/int(number),factorList)
        elif int(number) > int(num/2):
            break
    return factorList

def findFactorsNoDupes(num, primeList):
    factorList = []
    for number in primeList:
        if num % int(number) == 0:
            factorList.append(int(number))
        elif int(number) > int(num/2):
            break
    return factorList

def checkAgain(primeCheck,num,factorList):
    if (num) % primeCheck == 0:
        factorList.append(primeCheck)
        factorList = checkAgain(primeCheck,num/primeCheck,factorList)
        return factorList
    else:
        return factorList

def findCoprimes(functionResult,factorsList):
    coprimeResults = []
    for number in range(2,functionResult - 1):
        count = 0
        for item in factorsList:
            if number % item == 0:
                count += 1
                break
        if count == 0:
            coprimeResults.append(number)
    return(coprimeResults)
        
## FIND PUBLIC KEY (Relevant variables: primeOne,primeTwo,modulus,primes,fn,encryptionExponent,coprimes,publicKey)
def getFirstPrime(primeList):
    firstPrimeSlot = random.choice(primeList)
    return firstPrimeSlot

primeOne = getFirstPrime(primes)
print(primeOne)

primeTwo = getFirstPrime(primes)
print(primeTwo)

##      Modulus is the two primes times each other
modulus = primeOne * primeTwo
print(modulus)

##      fn is what we use to find the ENCRYPTION EXPONENT
fn = (primeOne - 1) * (primeTwo - 1)
print(fn)

factors = findFactorsNoDupes(fn,primes)
print(factors)


##      Finding the coprime we want to use
coprimes = findCoprimes(fn,factors)
encryptionExponent = random.choice(coprimes)

publicKey = [encryptionExponent, modulus]

print('Public Key: ', end = '')
print(publicKey)

## FIND PRIVATE KEY (Relevant variables: encryptionExponent, modulus,function)
## Function below outputs
def bruteForcePrime(encrypt,function):
    for integer in range(int((int(function)+1)/int(encrypt)),1000000000000000000):
        if (integer * encrypt) % function == 1:
            answer = integer
            break
    return answer

decryptionExponent = bruteForcePrime(encryptionExponent,fn)
privateKey = [decryptionExponent,modulus]
print('Private Key: ', end = '')
print(privateKey)

## User Interface
print('Encrypt = 1, Decrypt = 2')
choice = int(input())



## ENCRYPTION
if choice == 1:
    with open ('encrypt.txt','r') as encrypt:
        theLines = encrypt.readlines()
        testPhrase = theLines[0]
    for character in testPhrase:
        asciiPhrase.append(asciiDict[character])
    print(asciiPhrase)

if choice == 'test time': ## not using this rn
    for character in testPhrase:
        asciiPhrase.append(asciiDict[character])
    print(asciiPhrase)

if choice == 1:
    count = 0
    for character in asciiPhrase:
        asciiPhrase[count] = str((int(asciiPhrase[count]) ** encryptionExponent) % modulus)
        count += 1
print(asciiPhrase)

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
    print(asciiPhrase)

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
print(asciiPhrase)

if choice == 2:
    decryptedPhrase = ''
    for character in asciiPhrase:
        decryptedPhrase = decryptedPhrase + asciiDecryptionDict[int(character)]
    print(decryptedPhrase)

if choice == 2:
    with open ('encrypt.txt','w+') as encrypted:
        for character in asciiPhrase:
            encrypted.write(decryptedPhrase)

## test code below:
## factors = factors(primeMult,primes)
## print(factors)
