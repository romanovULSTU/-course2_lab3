
def vigenere(text, key, encrypt=True):
    result = ''
    for i in range(len(text)):
        letter_n = ord(text[i])
        key_n = ord(key[i % len(key)])
        if encrypt:
            value = (letter_n + key_n)
        else:
            value = (letter_n - key_n)
        result += chr(value)
    return result


def encrypt(text, key):
    return vigenere(text, key)


def decrypt(text, key):
    return vigenere(text, key, encrypt=False)