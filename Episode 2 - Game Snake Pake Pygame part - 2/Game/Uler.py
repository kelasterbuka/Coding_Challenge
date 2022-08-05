from Game import Kotak
import pygame

class Uler():
    badan = []
    kumpulan_arah = {} # sikey = posisi, valuenya = arah pergeraan

    def __init__(self,arena,start,arah_x=1,arah_y=0,warna=(0,0,255)):
        self.arena = arena
        self.start = start
        self.warna = warna
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.kepala = Kotak(arena,start,arah_x,arah_y,warna,nama="kepala")
        self.badan.append(self.kepala)

    def get_pos(self):
        return self.kepala.get_pos()

    def tambah_kotak(self):
        ekor = self.badan[-1]
        arah_x_ekor = ekor.get_arah_x()
        arah_y_ekor = ekor.get_arah_y()
        pos_ekor = ekor.get_pos()
        pos_ekor_x = pos_ekor[0]
        pos_ekor_y = pos_ekor[1]
        if arah_x_ekor == 1 and arah_y_ekor == 0:
            # lagi kekanan
            ekor_baru = Kotak(self.arena,(pos_ekor_x-1,pos_ekor_y),arah_x_ekor,arah_y_ekor)
            self.badan.append(ekor_baru)
        elif arah_x_ekor == -1 and arah_y_ekor == 0:
            # lagi kekiri
            ekor_baru = Kotak(self.arena,(pos_ekor_x+1,pos_ekor_y),arah_x_ekor,arah_y_ekor)
            self.badan.append(ekor_baru)

        elif arah_x_ekor == 0 and arah_y_ekor == 1:
            # lagi kebawah
            ekor_baru = Kotak(self.arena,(pos_ekor_x,pos_ekor_y-1),arah_x_ekor,arah_y_ekor)
            self.badan.append(ekor_baru)

        elif arah_x_ekor == 0 and arah_y_ekor == -1:
            # lagi keatas
            ekor_baru = Kotak(self.arena,(pos_ekor_x,pos_ekor_y+1),arah_x_ekor,arah_y_ekor)
            self.badan.append(ekor_baru)

    def reset(self):
        self.kepala = Kotak(self.arena,self.start,arah_x=1,warna=self.warna,nama="kepala")
        self.badan = []
        self.badan.append(self.kepala)
        self.kumpulan_arah = {}
        self.arah_x = 1
        self.arah_y = 0

    def move(self):
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_RIGHT]:
                self.arah_x = 1
                self.arah_y = 0
                self.kumpulan_arah[self.kepala.pos[:]] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_LEFT]:
                self.arah_x = -1
                self.arah_y = 0
                self.kumpulan_arah[self.kepala.pos] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_UP]:
                self.arah_x = 0
                self.arah_y = -1
                self.kumpulan_arah[self.kepala.pos] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_DOWN]:
                self.arah_x = 0
                self.arah_y = 1
                self.kumpulan_arah[self.kepala.pos] = [self.arah_x,self.arah_y]
        
        for index,kotak in enumerate(self.badan):
            pos_kotak = kotak.get_pos()
            if pos_kotak in self.kumpulan_arah:
                arah = self.kumpulan_arah[pos_kotak]
                arah_x = arah[0]
                arah_y = arah[1]
                kotak.move(arah_x,arah_y)
                if index == len(self.badan)-1:
                    self.kumpulan_arah.pop(pos_kotak)
            else:
                kotak.move(kotak.get_arah_x(),kotak.get_arah_y())

    def is_collide(self):
        pos_kepala = self.kepala.get_pos()
        is_collide = False;
        for index,kotak in enumerate(self.badan):
            if index > 0 and pos_kepala == kotak.get_pos():
                is_collide = True
                break
        
        return is_collide
        

    def draw(self):
        for anggota_badan in self.badan:
            anggota_badan.draw()