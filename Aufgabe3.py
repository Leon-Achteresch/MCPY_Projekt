class Saeuger:

    def __init__(self):
        self.variable01   = "public"
        self._variable02  = "protected"
        self.__variable03 = "private"
        self.variable04 = self.__variable03

class Mensch(Saeuger):

    def get_sichtbarkeitstest(self):
        test = "# Ausgabe get_sichtbarkeitstest(): {0:s}, {1:s}".format(
                self.variable01, self._variable02, self.variable04)
        return test

instanz = Mensch()
print(instanz.get_sichtbarkeitstest())

instanz = Saeuger()
print("# Ausgabe Saeuger(): {}".format(instanz.variable01))
print("# Ausgabe Saeuger(): {}".format(instanz._variable02))
print("# Ausgabe Saeuger(): {}".format(instanz.variable04))