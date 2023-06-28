#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hitung_gaji_pokok(golongan):
    if golongan == 'A':
        return 15000000
    elif golongan == 'B':
        return 10000000
    elif golongan == 'C':
        return 8000000
    elif golongan == 'D':
        return 5000000
    else:
        return 0

def hitung_gaji_total(golongan, jam_kerja):
    gaji_pokok = hitung_gaji_pokok(golongan)
    if jam_kerja > 48:
        gaji_lembur = (jam_kerja - 40) * (gaji_pokok / 40) * 1.5
        gaji_total = gaji_pokok + gaji_lembur
    else:
        gaji_total = gaji_pokok
    return gaji_total

while True:
    golongan = input("Masukkan Golongan Karyawan (A/B/C/D): ")
    jam_kerja = float(input("Masukkan Jam Kerja per Bulan: "))

    if golongan in ['A', 'B', 'C', 'D'] and jam_kerja >= 0:
        gaji_total = hitung_gaji_total(golongan, jam_kerja)
        print("Gaji Pokok Karyawan:", hitung_gaji_pokok(golongan))
        print("Gaji Total Karyawan:", gaji_total)
        break
    else:
        print("Input Tidak Valid. Silakan Coba Lagi.")


# In[ ]:




