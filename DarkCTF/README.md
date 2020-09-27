### Contents:
* OSINT
  * [Dark Social Web](https://github.com/jarp0l/CTF-Writeups/tree/master/DarkCTF#dark-social-web)
* Cryptography
  * [Pipe Rhyme](https://github.com/jarp0l/CTF-Writeups/tree/master/DarkCTF#pipe-rhyme)

# OSINT
## Dark Social Web
36 solves / 472 points
### Description:

0xDarkArmy has 1 social account and DarkArmy uses the same name everywhere. Hint: The front page of internet

flag format: darkctf{}

---

### Solution:

Searching for the username 0xDarkArmy (for example here: https://whatsmyname.app, and filter by category -> social) returns a result: https://www.reddit.com/user/0xDarkArmy

Scrolling down(if needed), there is a QR code marked as spoiler: https://www.reddit.com/user/0xDarkArmy/comments/iwal85/darkarmy_ctf/

Decoding that QR code gives a url which redirects to onion link: http://cwpi3mxjk7toz7i4.onion<br>
Part of the flag is on /robots.txt: http://cwpi3mxjk7toz7i4.onion/robots.txt<br>
Remaining part is on the response header 'flag' (Developer tools -> Network -> robots.txt -> Response headers).

Complete flag:
`darkctf{S0c1a1_D04k_w3b_051n7}`

<br>

[Go to Top](https://github.com/jarp0l/CTF-Writeups/tree/master/DarkCTF#contents)

---

# Cryptography
## Pipe Rhyme
221 solves / 249 points
### Description:
So special

[File](./files/pipeRhymeChall.txt)
***
In the file:

```
Chall:- Pipe Rhyme

Chall Desc:- Wow you are so special.

N=0x3b7c97ceb5f01f8d2095578d561cad0f22bf0e9c94eb35a9c41028247a201a6db95f
e=0x10001
ct=0x1B5358AD42B79E0471A9A8C84F5F8B947BA9CB996FA37B044F81E400F883A309B886
```

---

### Solution:
It is clear from the given values that it is a challenge related to RSA encrytion.
The following [python script](./files/pipeRhymeScript.py) gives the flag for this challenge:

```py
from Crypto.Util.number import inverse
from binascii import unhexlify

def main():
    # Given hex values, so converting to decimal:
    N = int('0x3b7c97ceb5f01f8d2095578d561cad0f22bf0e9c94eb35a9c41028247a201a6db95f', 16)
    e = int('0x10001', 16)
    ct = int('0x1B5358AD42B79E0471A9A8C84F5F8B947BA9CB996FA37B044F81E400F883A309B886', 16)

    # Factors of N, factored using factordb.com
    p = 31415926535897932384626433832795028841
    q = 56129192858827520816193436882886842322337671

    # Compute phi(n)
    phi = (p-1)*(q-1)

    # Compute modular inverse of e
    d = inverse(e, phi)

    # Decrypt ciphertext
    pt = pow(ct, d, N)  #equivalent to ct**d (mod N)
    # print("pt: " + str(pt))

    # Convert hex value from above to ASCII, that is, the original message
    print(bytearray.fromhex(hex(pt)[2:]).decode())

if __name__ == "__main__":
    main()
```

Flag: `darkCTF{4v0iD_us1ngg_p1_pr1mes}`

<br>

[Go to Top](https://github.com/jarp0l/CTF-Writeups/tree/master/DarkCTF#contents)
