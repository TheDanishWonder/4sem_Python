import webget

class TextContainer():

    def _init_(self, text):
        self.text = text
    
    def count_words(self):
        return len(self.text.split(" "))

    def countChars(self):
        return len(self.text)

    def countLetters(self):
        count = 0
        for char in self.text:
            if char in string.ascii_letters:
                count += 1
            return count

    def removePuntChars(self):
        for char in self.text:
            print(char)
            self.text = self.text.replace(char, '')
        return self.text
