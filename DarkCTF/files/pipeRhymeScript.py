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
