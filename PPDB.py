def ppdb():
    class nilai:
        def __init__(self, nama, no_abs,):
            self.nama = str(nama )
            self.absen = str(no_abs)
        def getNama(self):
            return self.nama
        def getAbsen(self):
            return self.absen
        def setNama(self, nama):
            self.nama = nama
        def setAbsen(self, no_abs):
            self.absen = no_abs

    Daftar_Siswa = {}
    loop = True

    print("================================================================================")
    print("              Selamat Datang Di Aplikasi Pendaftaran Siswa Baru                 ")
    print("================================================================================")
    print("                                     Menu                             ")
    print("1. Tambah Data       ")
    print("2. Hapus Data        ")
    print("3. Tampilkan Data    ")
    print("4. Cari Siswa        ")
    print("5. Edit Nama Siswa   ")
    print("6. Edit Nomor Siswa  ")
    print("7. Jumlah Total Siswa yang Sudah Mendaftar")
    print("0. Keluar            ")
    print("=================================================================================")

    while loop:
        print("\n")
        menu = input("Masukan Menu : ")
        if menu == "1":
            nama = input("Masukan Nama : ")
            absen = input("Masukan No Absen : ")
            siswa = nilai(nama, absen)
            Daftar_Siswa[absen] = siswa
        elif menu == "2":
            input("Masukan Nomer Absen Siswa : ")
            if absen in Daftar_Siswa:
                del Daftar_Siswa[absen]
            else:
                print("Data Tidak Ditemukan")
        elif menu == "3":
            for i in Daftar_Siswa:
                print("Nama Siswa : ", Daftar_Siswa[i].getNama())
                print("No Absen : ", Daftar_Siswa[i].getAbsen())
        elif menu == "4":
            absen = input("Masukan Nomor Absen Siswa : ")
            if absen in Daftar_Siswa:
                print("Nama Siswa : ", Daftar_Siswa[absen].getNama())
                print("Nomor Absen : ", Daftar_Siswa[absen].getAbsen())
            else:
                print("Data Tidak Ditemukan")
        elif menu == "5":
            absen = input("Masukan Nomor Absen Siswa : ")
            if absen in Daftar_Siswa:
                namaBaru = input("Masukan Nama Baru : ")
                Daftar_Siswa[absen].setNama(namaBaru)
            else:
                print("Data Tidak Ditemukan")
        elif menu == "6":
            absen = input("Masukan Nomor Absen Lama: ")
            if absen in Daftar_Siswa:
                absenBaru = input("Masukan Nomor Absen Baru : ")
                Daftar_Siswa[absen].setAbsen(absenBaru)
            else:
                print("Data Tidak Ditemukan")
        elif menu == "7":
            print("Jumlah Total Siswa: ", len(Daftar_Siswa))       
        elif menu == "0":
            loop = False
        else:
            print("Command not Found ")
            break
 
def biaya():
    print("Masukkan Pilihan Anda Dengan Jujur !")
    print ('1. Siswa Golongan 1 = Rp. 150.000 + 15%')
    print ('2. Siswa Golongan 2 = Rp. 150.000 + 10%')
    print ('3. Siswa Golongan 3 = Rp. 150.0000 + 5%')
    print ('4. Keluar ')
    while True : 
        daftar = int (input('Masukan Pilihan : '))
        if daftar == 1:
            nilai1 = 150000 + 150000/0.15
            print('Anda Dikenakan Biaya Sebesar : Rp.',nilai1) 
            break
        elif daftar == 2:
            nilai2 = 150000 + 150000/0.10
            print('Anda Dikenakan Biaya Sebesar : Rp.',nilai2)
            break 
        elif daftar == 3 :
            nilai3 = 150000 +  150000/0.05
            print('Anda Dikenakan Biaya Sebesar : Rp',nilai3)  
            break
        elif daftar == 4 :
            print("Program Selesai")
            break 
        else : 
            print("Masukkan Pilihan Dengan Benar!!")
    
while True :    
    print ('=======================')
    print ('Program PPDB')
    print ('=======================')
    print ('Masukan Menu')
    print ('1. Pendaftaran')
    print ('2. Pembayaran')
    print ('3. Matikan Program')
    print ('=======================')

    menu = int (input('Masukan Pilihan Anda : '))
    print()

    if menu == 1:
        ppdb()    
    if menu == 2:
        biaya()
    elif menu == 3:
        print ('Program Mati')
        break
    else:
        print('Tidak Ada Dalam Menu :')
    