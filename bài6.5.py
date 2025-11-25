class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()
        words.reverse()
        return " ".join(words)

s = ReverseWords("hello .py")
print(s.reverse())
