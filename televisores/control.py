class Control:

    def __init__(self):
        self.TV = None

    def turnOn(self):
        self.TV.turnOn()

    def turnOff(self):
        self.TV.turnOff()

    def canalUp(self):
        self.TV.canalUp()

    def canalDown(self):
        self.TV.canalDown()

    def canalUp(self):
        self.TV.canalUp()

    def volumeDown(self):
        self.TV.volumeDown()

    def volumenUp(self):
        self.TV.volumenUp()

    def setCanal(self, canal):
        self.TV.setCanal(canal)

    def enlazar(self, televisor):
        self.TV = televisor
        self.TV.setControl(self)

    def setTV(self, televisor):
        self.TV = televisor

    def getTv(self):
        return self.TV
