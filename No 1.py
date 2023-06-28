#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math

class BangunGeometri:
    def luas_Persegi(self, Sisi):
        return Sisi ** 2     

    def luas_Balok(self, Panjang, Lebar, Tinggi):
        return 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)

    def luas_Segitiga(self, Alas, Tinggi):
        return 0.5 * Alas * Tinggi

    def luas_Persegi_Panjang(self, Panjang, Lebar):
        return Panjang * Lebar
     
    def luas_Trapesium(self, Alas, Tinggi, sisi_Miring):
        return 0.5 * (Alas + sisi_Miring) * Tinggi 
    
    def luas_Lingkaran(self, Jari_Jari):
        return math.pi * jari_jari ** 2

bangun = BangunGeometri()

Sisi = 9
luas_Persegi = bangun.luas_Persegi(Sisi)
print("Luas Persegi:", luas_Persegi)

Panjang = 10
Lebar = 8
Tinggi = 3
luas_Balok = bangun.luas_Balok(Panjang, Lebar, Tinggi)
print("Luas Balok:", luas_Balok)

Alas = 14
Tinggi = 10
luas_Segitiga = bangun.luas_Segitiga(Alas, Tinggi)
print("Luas Segitiga:", luas_Segitiga)

Panjang = 7
Lebar = 4
luas_Persegi_Panjang = bangun.luas_Persegi_Panjang(Panjang, Lebar)
print("Luas Persegi Panjang:", luas_Persegi_Panjang)

Alas = 11
Tinggi = 5
sisi_Miring = 3
luas_Trapesium = bangun.luas_Trapesium(alas, Tinggi, sisi_Miring)
print("Luas Trapesium:", luas_Trapesium)

Jari_Jari = 12
luas_Lingkaran = bangun.luas_Lingkaran(Jari_Jari)
print("Luas Lingkaran:", luas_Lingkaran)


# In[ ]:




