class Animal:
    def __init__(self, name, makan, hidup, berkembangBiak):
        self.name = name
        self.makan = makan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print('Nama hewan adalah ', self.name)
        print('hewan ini pemakan ', self.makan)
        print('hewan ini hidup di  ', self.hidup)
        print('hewan ini berkembang biak dengan cara  ', self.berkembangBiak)
        

class Badak(Animal):
    def __init__(self, name, makan, hidup, berkembangBiak, keunikan):
        super().__init__(name, makan, hidup, berkembangBiak)
        self.keunikan = keunikan

    def print(self):
        super()
        print('keunikan badak adalah ', self.keunikan)

class Ikan(Animal):
    def __init__(self, name, makan, hidup, berkembangBiak, jenisikan):
         super().__init__(name, makan, hidup, berkembangBiak)
         self.jenisikan = jenisikan

    def print(self):
        super()
        print('jenis ikan adalah ', self.jenisikan)

class Ular(Animal):
    def __init__(self, name, makan, hidup, berkembangBiak, jenisular):
         super().__init__(name, makan, hidup, berkembangBiak)
         self.jenisular = jenisular

    def print(self):
        super()
        print('jenis ular adalah ', self.jenisular)

b = Badak('Badak bercula 1', 'Tumbuhan', 'darat', 'mamalia', 'bercula')
print('='*20)
print('DATA BADAK')
b.cetak()
b.print()

i = Ikan('ikan Nemo', 'cacing', 'air', 'bertelur', 'ikan laut')
print('='*20)
print('DATA IKAN')
i.cetak()
i.print()

u = Ular('Ular Kobra', 'Tikus', 'darat dan air', 'Bertelur', 'berbisa')
print('='*20)
print('DATA ULAR')
u.cetak()
u.print()