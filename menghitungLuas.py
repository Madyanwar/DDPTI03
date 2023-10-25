        luasSegitiga = 1/2 * alas * tinggi
        print("hasil dari luas segitiga dari", alas "dan", tinggi,  "adalah: ", luasSegitiga)print( '''selamat datang di penghitung luas bangun datar :
            1 = menghitung luas persegi.
            2 = menghitung luas lingkaran
            3 = menghitung luas segitiga ''')

pilih = int(input("masukan pilihan "))



match pilih:
    case 1:
        sisi = int(input("masukan sisi persegi: "))
        luasPersegi = sisi * sisi * sisi
        print("hasil dari luas persegi dari sisi", sisi ,"adalah: ", luasPersegi)
    case 2:
        J = int(input("masukan jari jari: "))
        luasLingkaran = 3.14 * J * J
        print("hasil dari luas lingkaran dari jari - jari", J , "adalah" ,luasLingkaran)
    case 3:
        alas = int(input("masukan alas: "))
        tinggi = int(input("masukan tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print("hasil dari luas segitiga dari alas ", alas, "dan tinggi ", tinggi,  "adalah: ", luasSegitiga)