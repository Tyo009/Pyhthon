def Fungsi(n, seed=1):
    a = 1103
    c = 1234
    m = 2 ** 31

    if n == 0:
        return seed

    Angka = Fungsi(n - 1, seed)

    Nomor = (a * Angka + c) % m

    return Nomor

# Calculate the value of the function when n = 100
Nilai = Fungsi(100)
print("Nilai dari n = 100 adalah:", Nilai)


# def Aritmatika(n):
#     Angka_Awal = 3
#     Selisih = 2
    
#     # Hitung angka ke-n
#     for _ in range(2, n+1):
#         Angka_Awal += Selisih
#         Selisih += 2
    
#     return Angka_Awal

# Nilai = Aritmatika(100)
# print("Angka ke-100 adalah:", Nilai)

