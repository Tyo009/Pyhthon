# greeting = 'Saya mulai belajar Python!'

# print(greeting)

# firstName= "Sigma"
# lastName= "Prasetyo"
# age=20
# isMarried = False

# print(firstName)
# print(lastName)
# print(age)
# print(isMarried)

# assert memoryview


# data_diri = {
#     "firstName" : "Sigma",
#     "lastName": "Prasetyo",
#     "age" : 20,
#     "isMarried" : False
# } 

# print(data_diri)

# kata = '                Sigma'.lstrip()


# print(kata)


# var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
# 179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
# 592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
# 950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
# 351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
# 175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
# 407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
# 605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
# 673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
# 235780, 857943, 605132, 125094, 620493, 913250
# ]

# panjang = len(var_list)
# minimal = (min(var_list))
# maksimal = (max(var_list))
# banyak = (var_list.count(605132))

# print(panjang)
# print(minimal)
# print(maksimal)
# print(banyak)

# Ekspresi

# """
# TODO:
# Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
# - Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
# - Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
# - Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
#   dan simpan dalam variabel bernama "total_harga".

# Tips:
# - Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
# """
# Jangan ubah kode ini

# dico = 750000
# total_harga = 0 

# if dico < 500000:
#     total_harga = dico-total_harga
#     print(total_harga)
# else:
#     dico >= 500000
#     total_harga = dico-(dico * 10/100)
#     print(int(total_harga))


# print (9//6)

# for i in range (10):
#     print(i)

# TODO: Silakan buat kode Anda di bawah ini.

# x =1
# y = 2

# temp = x

# x = y
# y = temp

# print (x)
# print (y)


# evenNumber = []
# num = 0

# while num <= 500:
#     if num % 2 == 0:
#         evenNumber.append(num)
#     num += 1
# print(evenNumber)


# for i in range(1, 3):    
#     for j in range(1, 3):    
#         print(i,j)





# x = [1, 2, 3, 4, 5]
# print(x)

# import array

# var_array = [i for i in range(101)]

# total_elements = 0
# total_sum = 0

# for num in var_array:
#     total_elements += 1
#     total_sum += num

# result = total_sum / total_elements

# print("Nilai rata-rata dari elemen array adalah:", result)

# var_arr= []
# print(var_arr)

# Matriks Blyat

# import numpy

# A = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

# print("Matrsik A adalah : ", A)


# penggunaan Matriks dalam Library Num dan Data
# import numpy 
# import sys

# var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

# print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
# print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# import numpy
# Matriks = numpy.array([[1,2,3],[5,6,7],[8,9,10,]])
# print(Matriks)

# Matriks = [[0 for i in range (4)] for i in range(3)]
# print(Matriks)

# var = [[5,0],
#        [1,-2]]

# def_mat = [[0 for j in range(2)] for i in range(2)]

# for i in range(len(var)):
#   for j in range(len(var[0])):
#     def_mat[i][j] = var[i][j]*2

#     print(def_mat)

# Belajar Fungsi 
 

# luas = 5
# lebar = 6

# luas_persegi_panjang = luas * lebar
# print(luas_persegi_panjang)

# Fungsi 
# def luas_persegi(panjang,lebar):
#     luas_persegi = panjang * lebar
#     return luas_persegi

# persegi_satu = luas_persegi(7,6)
# print(persegi_satu)


# def minimal(a,b):
#       if a < b:
#           return a
#       elif a > b:
#            return b
#       else :
#         a == b
#         return a

# minimalA = minimal(8,9) 
# minimalB = minimal(7,5) 
# samadengan = minimal(5,5)

# print(minimalA)
# print(minimalB)
# print(samadengan)

# OOP

# class Ayam:
#     Kaki = 2

# ayam = Ayam()
# print("Jumlah Kaki Ayam",ayam.Kaki)

# class Kereta: 
#     Roda = 16
#     Masinis = "tomo"

# kereta1 = Kereta()
# kereta1.Roda = 15
# kereta1.Masinis= "Tymo"

# print(kereta1.Masinis,kereta1.Roda)

# class Mobil:
#     def __init__(self, Klakson, Roda, Mesin):
#         self.Klakson = Klakson
#         self


# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
        
# mobil_1 = Mobil('Merah', 'DicodingCar', 160)

# print(mobil_1.warna)
# print(mobil_1.merek)
# print(mobil_1.kecepatan)


# kau at ikau 15/02/2024

# class KPU :
#     def __init__(self,jam,hari,kerja):
#         self.belajar = jam
#         self.mulai = hari
#         self.brutal = kerja

# # Kerja Rodi Paok


# Bekerja = KPU('3','Kamis','rodi')

# print(Bekerja.belajar)
# Bekerja.brutal = "romusha"
# print(Bekerja.brutal)

# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

#     def tambah_kecepatan(self):
#         self.kecepatan += 10

# mobil_1 = Mobil("Merah", "DicodingCar", 160)
# print("Sebelum ditambahkan: ")
# print(mobil_1.kecepatan)

# mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

# print("Setelah ditambahkan: ")
# print(mobil_1.kecepatan)


# class Animal:
#     name = "kumi"
#     age = 7
#     species = "cat"

    


# class Animal:
#     def __init__(self, name,age,species):
#         self.name = name
#         self.age = age
#         self.species = species

# Sapi = Animal("Moko",12,"Animal")


# print("Nama Sapi Adalah",Sapi.name)
# print("Umur Sapi Tersebut",Sapi.age)
# print("Termasuk Species",Sapi.species)


# class Cat(Animal):
#     def deskripsi(self):
#         self.name
#         self.age 
#         self.species 

#     def suara(self):
#         return "Meow"

# Kucing = Cat("Neko",7,"Persian")

# print("Kucing Saya Bernama", Kucing.name)
# print("Kucing Saya Berumur", Kucing.age)
# print("Kucing Saya Berspesies", Kucing.species)
# print("Kucing Saya Bersuara", Kucing.suara())


# class Kalkulator:
#     """kalkulator tambah kurang"""
#     def __init__(self, _i):
#         self.i = _i
#     def tambah(self, _i): return self.i + _i
#     def kurang(self, _i):
#         return self.i - _i

# import unittest
 
# class TestStringMethods(unittest.TestCase):
#     # Ini adalah test case pertama (1)
#     def test_strip(self):
#         self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
#     # Test case kedua (2)
#     def test_isalnum(self):
#         self.assertTrue('c0d1ng'.isalnum())
#         self.assertFalse('c0d!ng'.isalnum())
    
#     # Test case ketiga (3)
#     def test_index(self):
#         s = 'dicoding'
#         self.assertEqual(s.index('coding'), 2)
#         # cek s.index gagal ketika tidak ditemukan
#         with self.assertRaises(ValueError):
#             s.index('decode')
    
# if __name__ == '__main__':
#     # Test Runner
#     unittest.main()


# import unittest
 
# def koneksi_ke_db():
#     print("[terhubung ke db]")
 
# def putus_koneksi_db(db):
#     print("[tidak terhubung ke db {}]".format(db))
 
# class User:
#     username = ""
#     aktif = False
 
#     def __init__(self, db, username):  # using db sample
#         self.username = username
 
#     def set_aktif(self):
#         self.aktif = True
 
# class TestUser(unittest.TestCase):
#     # Test Case 1
#     def test_user_default_not_active(self):
#         db = koneksi_ke_db()
#         dicoding = User(db, "dicoding")
#         self.assertFalse(dicoding.aktif)  # tidak aktif secara default
#         putus_koneksi_db(db)
 
#     # Test Case 2
#     def test_user_is_active(self):
#         db = koneksi_ke_db()
#         dicoding = User(db, "dicoding")
#         dicoding.set_aktif()  # aktifkan user baru
#         self.assertTrue(dicoding.aktif)
#         putus_koneksi_db(db)
 
# if __name__ == "__main__":
#     # Test Runner
#     unittest.main()

# import matplotlib.pyplot as plt
 
# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
 
# # Membuat plot garis
# plt.plot(x, y)
 
# # Menambahkan judul dan label sumbu
# plt.title("Contoh Plot Garis")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
 
# # Menampilkan plot
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt
 
# # Contoh data
# tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# # Contoh plot histogram
# sns.histplot(tips['total_bill'], kde=True)
# plt.title('Histogram Total Bill')
# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.show()


# x = { 'name': 'Coding', 'age': 20, 'isMarried': False }
# x ['name'] = "Dicoding"
# print(x)

# x = [1, 2.2, 'Dicoding']
# x[0] = 'Indonesia'
# print(x)

# x = 1960 
# y = 901 
# print(x % y) 


# x = "Belajar" 
# y = "Python" 
# result = x > y 
# print(result) 

# variabel_pertama = "Dicoding"
# VariAbel_Pertama = "Indonesia"

# print(variabel_pertama)
# print(VariAbel_Pertama)
# print(VARIABEL_PERTAMA)


# x = { 'name': 'Coding', 'age': 20, 'isMarried': False }
# x ['name'] = "Dicoding"
# print(x)