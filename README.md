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
2. Alice chooses a secret key a = 4, then sends Bob a public key A = g<sup>a</sup> mod p  
A = 5<sup>4</sup> mod 23 = 4
3. Bob chooses a secret key b = 3, then sends Alice a public key B = g<sup>b</sup> mod p  
B = 5<sup>3</sup> mod 23 = 10
4. Alice uses Bob's public key and her private key to compute a shared secret s = B<sup>a</sup> mod p  
s = 10<sup>4</sup> mod 23 = 18
5. Bob uses Alice's public key and his private key to compute the same shared secret s = Ab mod p  
s = 4<sup>3</sup> mod 23 = 18
6. Alice and Bob now share a secret (the number 18), which can be used as a key to do symmetric encryption on large pieces of content. 

## References
[https://en.wikipedia.org/wiki/Public-key_cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)
[https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)