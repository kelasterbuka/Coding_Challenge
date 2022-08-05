from asyncio import start_unix_server
import pygame

class Kotak():
    
    def __init__(self,arena,pos_awal,arah_x=1,arah_y=1,warna=(0,0,255)):
        self.pos = pos_awal
        self.arah_x = arah_x # arah positif kanan
        self.arah_y = arah_y # arah positif bawah
        self.warna = warna
        self.surface = arena.get_surface()
        self.lebar = arena.get_jarak_kolom()
        self.tinggi = arena.get_jarak_baris()
        self.arena = arena
        arena.assign(self)

    def move(self,arah_x,arah_y):
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.pos = (self.pos[0] + self.arah_x, self.pos[1] + self.arah_y)

        if self.pos[0] == self.arena.get_jumlah_kolom():
            self.pos = (0,self.pos[1])
        elif self.pos[0] < 0:
            self.pos = (self.arena.get_jumlah_kolom()-1,self.pos[1])

        if self.pos[1] == self.arena.get_jumlah_baris():
            self.pos = (self.pos[0],0)
        elif self.pos[1] < 0:
            self.pos = (self.pos[0],self.arena.get_jumlah_baris()-1)

    def draw(self):
        start_x = self.lebar*self.pos[0]
        start_y = self.tinggi*self.pos[1]
        pygame.draw.rect(self.surface, self.warna,(start_x,start_y,self.lebar,self.tinggi))

