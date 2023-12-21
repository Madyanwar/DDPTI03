class orang:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def makan(self):
        print('saya bisa makan')

    def cetak(self):
        print('Nama Saya ', self.fname, self.lname)

class mahasiswa(orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan
    def print(self):
        super().cetak()
        print('Saya prodi ', self.prodi, "saya angkatan ", self.angkatan)

class pegawai(orang):
    def bekerja(self):
        print("Saya bekerja")

x = orang('Ade', "Firmansyah")
x.cetak()

y = mahasiswa('dwi', 'astuti', 'Teknik Informatika', 2023)
y.print()
y.makan()

z = pegawai('Agus', 'Rahman')
z.bekerja()