def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print('Luas Persegi: ', luas)
    print('Keliling Persegi: ', keliling)

def persegipanjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * panjang + lebar
    print('Luas Persegi  Panjang: ', luas)
    print('Keliling Persegi Panjang: ', keliling)

def lingkaran(jarijari):
    phi = 3.14
    luas = phi * jarijari * jarijari
    keliling = 2 * phi * jarijari
    print('Luas Lingkaran: ', luas)
    print('Keliling Lingkaran: ', keliling)

def segitiga_sama_sisi(alas, tinggi):
    luas = 0.5 * alas * tinggi 
    keliling = alas * 3
    print('Luas Segitiga Sama sisi: ', luas)
    print('Keliling Segitiga Sama sisi: ', keliling)

def belah_ketupat(d1, d2, sisi):
    luas = 0.5 * d1 * d2
    keliling = 4 * sisi
    print('Luas Belah Ketupat: ', luas)
    print('Keliling Belah Ketupat: ', keliling)

def jajar_genjang(alas, tinggi, sisib):
    luas = alas * tinggi
    keliling = 2 * alas + 2 * sisib
    print('Luas Jajar Genjang: ', luas)
    print('Keliling Jajar Genjang: ', keliling)

def layang_layang(d1, d2, sisi_atas, sisi_bawah):
    luas = d1 * d2 * 0.5
    keliling = (sisi_atas * 2) + (sisi_bawah * 2)
    print('Luas SLAyang Layang: ', luas)
    print('Keliling LAyang Layang: ', keliling)