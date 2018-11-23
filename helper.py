import random
# import primes
# We don't actually need a separate primes.py because there is some
# fancy footwork below that extracts primes from python.txt file

# TODO: describe each of the variables
primeMult = 189027348
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
    # print(imprt)
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
    # print(asciiDict)

## SETTING UP DECRYPTION DICTIONARY
asciiDecryptionDict = {
    }
for item in asciiDict:
    asciiDecryptionDict[asciiDict[item]] = item
# print(asciiDecryptionDict)


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

## FIND PRIVATE KEY (Relevant variables: encryptionExponent, modulus,function)
def bruteForcePrime(encrypt,function):
    for integer in range(int((int(function)+1)/int(encrypt)),1000000000000000000):
        if (integer * encrypt) % function == 1:
            answer = integer
            break
    return answer