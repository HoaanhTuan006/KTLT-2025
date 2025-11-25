class StringDemo:
    def get_String(self):
        self.s = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.s.upper())

obj = StringDemo()
obj.get_String()
obj.print_String()
