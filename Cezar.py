import string

def cezar(text: str, key: int) -> str:
    alphabet = string.ascii_lowercase
    code = alphabet[key:] + alphabet[:key]
    translate = str.maketrans(alphabet, code)
    return text.translate(translate)
    # return ''.join([chr(ord(litera) + klucz) for litera in napis])

print(cezar('xyz', 3))
