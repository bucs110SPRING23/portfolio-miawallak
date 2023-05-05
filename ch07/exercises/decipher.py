
ciphertext = "ZYF HRUKB NLAXJ OAC VRTPD AWFL ZYF GIMQ EAS"
shift = 5

plaintext = ""

for char in ciphertext:
    if char == " ":
        plaintext += " "
    elif char.isalpha():
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        shifted = (ord(char) - start - shift) % 26 + start
        plaintext += chr(shifted)
    else:
        pass

with open('decrypted.txt', 'w') as f:
    f.write(plaintext)
