from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
from Issiz import Issiz
from Insan import Insan
import pandas as pd


insan1 = Insan("12345678901", "Ahmet", "Yılmaz", 35, "Erkek", "Türk")
insan2 = Insan("09876543210", "Ayşe", "Kaya", 28, "Kadın", "Türk")
print(insan1)
print("**************************************")
print(insan2)
print("**************************************")

issiz1 = Issiz("12345678901", "Mehmet", "Demir", 40, "Erkek", "Türk", {"mavi yaka": 5, "beyaz yaka": 3, "yönetici": 8})
issiz2 = Issiz("09876543210", "Fatma", "Yıldız", 32, "Kadın", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
issiz3 = Issiz("13579246801", "Ali", "Can", 45, "Erkek", "Türk", {"mavi yaka": 3, "beyaz yaka": 5, "yönetici": 10})
print(issiz1)
print("**************************************")
print(issiz2)
print("**************************************")
print(issiz3)
print("**************************************")

calisan1 = Calisan("12345678901", "Bekir", "Yılmaz", 28, "Kadın", "Türk", "teknoloji", 18, 12000)
calisan2 = Calisan("09876543210", "İlyas", "Kaya", 32, "Erkek", "Türk", "muhaebe", 36, 18000)
calisan3 = Calisan("13579246801", "Mahmut", "Demir", 40, "Erkek", "Türk", "inşaat", 48, 22000)
print(calisan1)
print("**************************************")
print(calisan2)
print("**************************************")
print(calisan3)
print("**************************************")

maviyaka1 = MaviYaka("12345678901", "Veli", "Yıldız", 35, "Kadın", "Türk", "teknoloji", 24, 15000, 0.2)
maviyaka2 = MaviYaka("09876543210", "Rıdvan", "Can", 42, "Erkek", "Türk", "muhaebe", 18, 12000, 0.15)
maviyaka3 = MaviYaka("13579246801", "Emine", "Kaya", 28, "Kadın", "Türk", "inşaat", 12, 10000, 0.1)
print(maviyaka1)
print("**************************************")
print(maviyaka2)
print("**************************************")
print(maviyaka3)
print("**************************************")

beyazyaka1 = BeyazYaka("12345678901", "Fırat", "Kaya", 32, "Erkek", "Türk", "teknoloji", 1, 15000, 1000)
beyazyaka2 = BeyazYaka("09876543210", "Kerem", "Demir", 40, "Erkek", "Türk", "muhaebe", 5, 12000, 800)
beyazyaka3 = BeyazYaka("13579246801", "Faruk", "Yıldız", 35, "Kadın", "Türk", "inşaat", 12, 10000, 500)
print(beyazyaka1)
print("**************************************")
print(beyazyaka2)
print("**************************************")
print(beyazyaka3)




data = {
    "Nesne" : ["Calisan1","Calisan2","Calisan3","MaviYaka1","MaviYaka2","MaviYaka3","BeyazYaka1","BeyazYaka2","BeyazYaka3"],
    "TC No" : [calisan1.get_tc_no(),calisan2.get_tc_no(),calisan3.get_tc_no(),maviyaka1.get_tc_no(),maviyaka2.get_tc_no(),maviyaka3.get_tc_no(),beyazyaka1.get_tc_no(),beyazyaka2.get_tc_no(),beyazyaka3.get_tc_no()],
    "Ad"    : [calisan1.get_ad(),calisan2.get_ad(),calisan3.get_ad(),maviyaka1.get_ad(),maviyaka2.get_ad(),maviyaka3.get_ad(),beyazyaka1.get_ad(),beyazyaka2.get_ad(),beyazyaka3.get_ad()],
    "Soyad" : [calisan1.get_soyad(),calisan2.get_soyad(),calisan3.get_soyad(),maviyaka1.get_soyad(),maviyaka2.get_soyad(),maviyaka3.get_soyad(),beyazyaka1.get_soyad(),beyazyaka2.get_soyad(),beyazyaka3.get_soyad()],
    "Yaş"   : [calisan1.get_yas(),calisan2.get_yas(),calisan3.get_yas(),maviyaka1.get_yas(),maviyaka2.get_yas(),maviyaka3.get_yas(),beyazyaka1.get_yas(),beyazyaka2.get_yas(),beyazyaka3.get_yas()],
    "Cinsiyet"  : [calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan3.get_cinsiyet(),maviyaka1.get_cinsiyet(),maviyaka2.get_cinsiyet(),maviyaka3.get_cinsiyet(),beyazyaka1.get_cinsiyet(),beyazyaka2.get_cinsiyet(),beyazyaka3.get_cinsiyet()],
    "Uyruk" : [calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviyaka1.get_uyruk(),maviyaka2.get_uyruk(),maviyaka3.get_uyruk(),beyazyaka1.get_uyruk(),beyazyaka2.get_uyruk(),beyazyaka3.get_uyruk()],
    "Sektör": [calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),maviyaka1.get_sektor(),maviyaka2.get_sektor(),maviyaka3.get_sektor(),beyazyaka1.get_sektor(),beyazyaka2.get_sektor(),beyazyaka3.get_sektor()],
    "Tecrübe": [calisan1.get_tecrube(),calisan2.get_tecrube(),calisan3.get_tecrube(),maviyaka1.get_tecrube(),maviyaka2.get_tecrube(),maviyaka3.get_tecrube(),beyazyaka1.get_tecrube(),beyazyaka2.get_tecrube(),beyazyaka3.get_tecrube()],
    "Maaş"  : [calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),maviyaka1.get_maas(),maviyaka2.get_maas(),maviyaka3.get_maas(),beyazyaka1.get_maas(),beyazyaka2.get_maas(),beyazyaka3.get_maas()],
    "Yipranma Payi" : [0,0,0,maviyaka1.get_yipranma_payi(),maviyaka2.get_yipranma_payi(),maviyaka3.get_yipranma_payi(),0,0,0],
    "Teşvik Primi"  : [0,0,0,0,0,0,beyazyaka1.get_tesvik_primi(),beyazyaka2.get_tesvik_primi(),beyazyaka3.get_tesvik_primi()],
    "Yeni Maaş"  :[calisan1.get_maas()+calisan1.zam_hakki(),calisan2.get_maas()+calisan2.zam_hakki(),calisan3.get_maas()+calisan3.zam_hakki(),maviyaka1.get_maas()+maviyaka1.zam_hakki(),maviyaka2.get_maas()+maviyaka2.zam_hakki(),maviyaka3.get_maas()+maviyaka3.zam_hakki(),beyazyaka1.get_maas()+beyazyaka1.zam_hakki(),beyazyaka2.get_maas()+beyazyaka2.zam_hakki(),beyazyaka3.get_maas()+beyazyaka3.zam_hakki()]
}
df=pd.DataFrame(data)
print(df)
#Calisan, MaviYaka, BeyazYaka grupları için ayrı ayrı tecrübe ve yeni maaş ortalamalarını bulduk
calisanlar_tecrube = [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube()]
calisanlar_yeni_maas = [calisan1.get_maas() + calisan1.zam_hakki(), calisan2.get_maas() + calisan2.zam_hakki(), calisan3.get_maas() + calisan3.zam_hakki()]

mavi_yaka_tecrube = [maviyaka1.get_tecrube(), maviyaka2.get_tecrube(), maviyaka3.get_tecrube()]
mavi_yaka_yeni_maas = [maviyaka1.get_maas() + maviyaka1.zam_hakki(), maviyaka2.get_maas() + maviyaka2.zam_hakki(), maviyaka3.get_maas() + maviyaka3.zam_hakki()]

beyaz_yaka_tecrube = [beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(), beyazyaka3.get_tecrube()]
beyaz_yaka_yeni_maas = [beyazyaka1.get_maas() + beyazyaka1.zam_hakki(), beyazyaka2.get_maas() + beyazyaka2.zam_hakki(), beyazyaka3.get_maas() + beyazyaka3.zam_hakki()]

calisan_tecrube_ort = sum(calisanlar_tecrube) / len(calisanlar_tecrube)
calisan_yeni_maas_ort = sum(calisanlar_yeni_maas) / len(calisanlar_yeni_maas)

mavi_yaka_tecrube_ort = sum(mavi_yaka_tecrube) / len(mavi_yaka_tecrube)
mavi_yaka_yeni_maas_ort = sum(mavi_yaka_yeni_maas) / len(mavi_yaka_yeni_maas)

beyaz_yaka_tecrube_ort = sum(beyaz_yaka_tecrube) / len(beyaz_yaka_tecrube)
beyaz_yaka_yeni_maas_ort = sum(beyaz_yaka_yeni_maas) / len(beyaz_yaka_yeni_maas)

print("Çalışanlar İçin:")
print("Tecrübe Ortalaması:", calisan_tecrube_ort)
print("Yeni Maaş Ortalaması:", calisan_yeni_maas_ort)

print("Mavi Yaka İçin:")
print("Tecrübe Ortalaması:", mavi_yaka_tecrube_ort)
print("Yeni Maaş Ortalaması:", mavi_yaka_yeni_maas_ort)

print("Beyaz Yaka İçin:")
print("Tecrübe Ortalaması:", beyaz_yaka_tecrube_ort)
print("Yeni Maaş Ortalaması:", beyaz_yaka_yeni_maas_ort)


#  Maaşı(yeni maaş değil) 15000 TL üzerinde olanların toplam sayısı
maas_ust_limit = 15000
toplam_maaş_ust_limit = df[df["Maaş"] > maas_ust_limit].shape[0]
print("\nMaaşı 15000 TL üzerinde olanların toplam sayısı:", toplam_maaş_ust_limit)

#  Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
df_sirali = df.sort_values("Yeni Maaş")
print("\nYeni Maaşa göre sıralanmış DataFrame:")
print(df_sirali)

#  Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
beyaz_yakalar = df[(df["Nesne"].str.startswith("BeyazYaka")) & (df["Tecrübe"] > 3)]
print("\nTecrübesi 3 seneden fazla olan Beyaz yakalılar:")
print(beyaz_yakalar)

#  Yeni DataFrame oluşturma
yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
print("\nYeni DataFrame:")
print(yeni_df)







