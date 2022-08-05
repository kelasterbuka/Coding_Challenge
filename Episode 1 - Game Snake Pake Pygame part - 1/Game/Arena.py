import pygame

class Arena():
    
    def __init__(self,arena_lebar,arena_tinggi,jumlah_baris,jumlah_kolom):
        pygame.init()
        self.arena_lebar = arena_lebar
        self.arena_tinggi = arena_tinggi
        self.jumlah_baris = jumlah_baris
        self.jumlah_kolom = jumlah_kolom
        self.jarak_baris = self.arena_lebar // self.jumlah_baris
        self.jarak_kolom = self.arena_tinggi // self.jumlah_kolom
        self.clock = pygame.time.Clock()
        self.objects = []
        
        self.surface = pygame.display.set_mode((self.arena_lebar,self.arena_tinggi))


    def assign(self,object):
        self.objects.append(object)
    
    def get_surface(self):
        return self.surface

    def get_jarak_baris(self):
        return self.jarak_baris
    
    def get_jarak_kolom(self):
        return self.jarak_kolom

    def get_jumlah_kolom(self):
        return self.jumlah_kolom

    def get_jumlah_baris(self):
        return self.jumlah_baris

    def draw_grid(self):
        for baris_ke in range(self.jumlah_baris):
            x = self.jarak_baris*baris_ke
            y = self.jarak_kolom*baris_ke
            pygame.draw.line(self.surface,(0,0,0),(x,0),(x,self.arena_tinggi))
            pygame.draw.line(self.surface,(0,0,0),(0,y),(self.arena_lebar,y))

    def render(self,fps):
        self.surface.fill((255,255,255))
        for obj in self.objects:
            obj.draw()

        self.draw_grid()
        pygame.display.update()
        pygame.time.delay(50)
        self.clock.tick(fps)



