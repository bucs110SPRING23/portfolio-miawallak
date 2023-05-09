class StringUtility:
  
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        vowels = "aeiou"
        count = sum(1 for char in self.string if char in vowels)
        if count < 5:
            return str(count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return self.string[:2] + self.string[-2:]

    def fixStart(self):
        if len(self.string) <= 1:
            return self.string
        else:
            return self.string[0] + self.string[1:].replace(self.string[0], "*")

    def asciiSum(self):
        return sum(ord(char) for char in self.string)

    def cipher(self):
        encoded = ""
        for char in self.string:
            if char.isalpha():
                start = ord('b') if char.islower() else ord('B')
                offset = ord(char) - start
                encoded_char = chr((offset + len(self.string)) % 26 + start)
            else:
                encoded_char = char
            encoded += encoded_char
        return encoded