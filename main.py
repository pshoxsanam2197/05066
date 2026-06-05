class Hayvon:
    def __init__(self, tur):
        self.__tur = tur

    def get_tur(self):
        return self.__tur

    def set_tur(self, tur):
        self.__tur = tur

h = Hayvon("Mushuk")
print(h.get_tur())

h.set_tur("It")
print(h.get_tur())
