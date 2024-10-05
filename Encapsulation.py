#__ for private _ for protected
class Password:
    def __init__(self, chars):
        self.__chars = chars

    def setter_chars(self, morechars):
        self.__chars += morechars

    def getter_chars(self):
        return self.__chars


pw = Password('abc')
pw.setter_chars('123')
print(pw.getter_chars())



