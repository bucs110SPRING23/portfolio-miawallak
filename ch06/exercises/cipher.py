def caesar_cipher(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-shift] + alphabet[0:(26-shift)]
    result = ""
    for char in text:
        if char .isupper(): 
            result = result + shifted_alphabet
        else:
            result = result + shifted_alphabet 
        return result 
    
text = "The quick brown fox jumps over the lazy dog"
s = 6

print("Plain Text:", text)
print("Shift Pattern:", str(s))
print("Cipher:", caesar_cipher)

