from Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.__yipranma_payi * 10
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return self.get_maas() * self.get_tecrube() / 200 + (self.__yipranma_payi * 10)
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return self.get_maas() * self.get_tecrube() / 300 + (self.__yipranma_payi * 10)

    def __str__(self):
        return f"{super().__str__()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {self.get_maas() + self.zam_hakki()}"