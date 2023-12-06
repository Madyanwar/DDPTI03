import math

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil tambah dari ",angka1, "+", angka2 ,"adalah: ",hasil)

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print("Hasil kurang dari ",angka1, "-", angka2, "adalah: ", hasil)

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil kali dari ",angka1, "*", angka2, "adalah: ", hasil)

def bagi(angka1, angka2):
    hasil = angka1 / angka2
    print("Hasil bagi dari ",angka1, "/", angka2, "adalah: ", hasil)

def pangkat(angka1, angka2):
    hasil = angka1 ** angka2
    print("Hasil pemangkatan dari ",angka1, "^", angka2, "adalah: ", hasil)

def sisabagi(angka1, angka2):
    hasil = angka1 % angka2
    print('Hasil sisa bagi dari ', angka1, "%", angka2, 'Adalah: ', hasil)

def hasilbagi(angka1, angka2):
    hasil = angka1 // angka2
    print('Hasil bagi dari ', angka1, "//", angka2, 'Adalah: ', hasil)

def faktorial(angka1):
    hasil = math.factorial(angka1)
    print("hasil dari faktorial ", angka1, 'adalah: ', hasil)

def log10(angka1):
    hasil = math.log10(angka1)
    print('Hasil log10 dari ', angka1, 'Adalah: ', hasil)

def sin(angka1):
    hasil = math.sin(angka1)
    print('Hasil sin dari ', angka1, 'Adalah: ', hasil)