class przeciwnik():
    def __init__(self,sz,strzal,ruch,wybuch):
        self.rozmiar = sz
        self.umiejetnosc = strzal
        self.pozycja = ruch
        self.otrzymanie_obrazen = wybuch #zmiana skórki
        self.wytrzymalosc = 1
    def otrzymanie_obrazen(self,wybuch):
        self.otrzymanie_obrazen = wybuch
    def get_wytrzymalosc(self):
        return self.wytrzymalosc
    def set_wytrzymalosc(self,hp):
        self.wytrzymalosc = hp
    def otrzymanie_obrazen(self):
        self.otrzymanie_obrazen -=1
        print ("wybuch")
        return otrzymanie_obrazen
