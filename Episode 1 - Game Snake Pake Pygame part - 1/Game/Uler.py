from Game import Kotak

class Uler():
    badan = []
    def __init__(self,arena,start):
        self.arena = arena
        self.kepala = Kotak(arena,start)
        self.badan.append(self.kepala)

    def tambah_kotak(self,posisi):
        badan_baru = Kotak(self.arena,posisi)
        self.badan.append(badan_baru)

    def move(self,arah_x,arah_y):
        for anggota_badan in self.badan:
            anggota_badan.move(arah_x,arah_y)

    def draw(self):
        for anggota_badan in self.badan:
            anggota_badan.draw()