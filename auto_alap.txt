class Híres_auto:
    def __init__(self, márka_név, henger_térfogatát,orszag):
        self.név = márka_név
        self.henger_térfogat = henger_térfogatát
        self.orszag = orszag
    def nemzet(self):
        if (self.orszag == "n"):
            return "német"
        else:
            return "japán"


