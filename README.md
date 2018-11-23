# Asymmetric Cryptographic Example
This is an example of asymmetric cryptography with both an encryption and decryption method.

## Requirements to run
Python 3 and above.

## Getting Started
```
git clone url
python main.py
```
Then enter an option to either encrypt the contents of encrypt.txt file or decrypt the contents of decrypt.txt

## Cryptographic explanation
The simplest and the original implementation of the first asymmetric cryptographic protocol uses the multiplicative group of integers modulo p, where p is prime, and g is a primitive root modulo p. These two values are chosen in this way to ensure that the resulting shared secret can take on any value from 1 to p–1. Here is an example of the protocol.

1. Alice and Bob agree to use a modulus p = 23 and base g = 5 (which is a primitive root modulo 23).
2. Alice chooses a secret integer a = 4, then sends Bob A = g<sup>a</sup> mod p  
A = 5<sup>4</sup> mod 23 = 4
3. Bob chooses a secret integer b = 3, then sends Alice B = g<sup>b</sup> mod p  
B = 5<sup>3</sup> mod 23 = 10
4. Alice computes s = B<sup>a</sup> mod p  
s = 10<sup>4</sup> mod 23 = 18
5. Bob computes s = Ab mod p  
s = 4<sup>3</sup> mod 23 = 18
6. Alice and Bob now share a secret (the number 18).  

## References
[https://en.wikipedia.org/wiki/Public-key_cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)
[https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)