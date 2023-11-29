daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def duplikat(daftar_buah):
    hasil = []
    for buah in daftar_buah:
        hasil.extend([buah, buah])
    return hasil

print(duplikat(daftar_buah))
