angka = 2
x = int(input("Masukan Nilai Anda : "))

for i in range(1, x + 1):
    cetak = False
    while True:   
        faktor = 0
        pembagi = 1

        while True:   
            if angka % pembagi == 0:
                faktor = faktor + 1
            pembagi = pembagi + 1
            if not(pembagi <= angka): break  
        if faktor == 2:
            print(angka)
            cetak = True
        angka = angka + 1
        if not(cetak == False): break  
