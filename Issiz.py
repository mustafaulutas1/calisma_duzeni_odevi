from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu_gecmisi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu_gecmisi = statu_gecmisi

    def get_statu_gecmisi(self):
        return self.__statu_gecmisi

    def set_statu_gecmisi(self, statu_gecmisi):
        self.__statu_gecmisi = statu_gecmisi

    def statu_bul(self):
        max_etki = 0
        en_uygun_statu = ""
        for statu, yil in self.__statu_gecmisi.items():
            if statu == "mavi yaka":
                etki = yil * 0.2
            elif statu == "beyaz yaka":
                etki = yil * 0.35
            elif statu == "yönetici":
                etki = yil * 0.45
            else:
                etki = 0

            if etki > max_etki:
                max_etki = etki
                en_uygun_statu = statu

        return en_uygun_statu

    def __str__(self):
        return f"{super().__str__()}\nEn Uygun Statü: {self.statu_bul()}"