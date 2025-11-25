class RomanToInt:
    def __init__(self, roman):
        self.roman = roman

    def convert(self):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50,
                      'C':100, 'D':500, 'M':1000}
        total = 0
        i = 0

        while i < len(self.roman):
            if i+1 < len(self.roman) and roman_dict[self.roman[i]] < roman_dict[self.roman[i+1]]:
                total += roman_dict[self.roman[i+1]] - roman_dict[self.roman[i]]
                i += 2
            else:
                total += roman_dict[self.roman[i]]
                i += 1
        return total

r = RomanToInt("MCMXCIV")
print(r.convert())
