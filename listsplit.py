

class Kast(object):
    # self is nog niks dat gebeurt pas aan het eind
    def __init__(self,naam):
        # self is nog niks dat gebeurt pas aan het eind
        self.naam=naam
        self.dicht = True
        # self is nog niks dat gebeurt pas aan het eind
    def open(self):
        # self is nog niks dat gebeurt pas aan het eind
        if self.dicht == False:
            print("Ik ben open",self.naam)
        else:
            # self is nog niks dat gebeurt pas aan het eind
            self.dicht = False
            print('Ik ben al open', self.naam)

    def sluit(self):
        # self is nog niks dat gebeurt pas aan het eind
        if self.dicht:
            # self is nog niks dat gebeurt pas aan het eind
            print("Kast is nu dicht")
            # self is nog niks dat gebeurt pas aan het eind
        else: self.dicht = False
        print("Ik ben open en niet dicht")
        # self is nog niks dat gebeurt pas aan het eind
        self.dicht = True



class Kledingkast(Kast):

    def __init__(self, naam):
        self.lamp = False
       super().__init__(naam)
    self.lamp = False

    def sluit(self):



g=Kast("Mark")
g.open()
g.dicht=True
g.open()