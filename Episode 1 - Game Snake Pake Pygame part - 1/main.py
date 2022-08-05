# tiap nambah 10 makanan nambah speed
# Todo: 
# init
import pygame
from Game import Arena,Kotak,Uler

arena = Arena(500,500,20,20)
uler = Uler(arena,(10,10))
#simulasi ketemu makanan
uler.tambah_kotak((9,10))
uler.tambah_kotak((8,10))
isRun = True
arah_x = 0
arah_y = 0
while isRun:
    # user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_RIGHT]:
            arah_x = 1
            arah_y = 0
        elif keys[pygame.K_LEFT]:
            arah_x = -1
            arah_y = 0
        elif keys[pygame.K_UP]:
            arah_x = 0
            arah_y = -1
        elif keys[pygame.K_DOWN]:
            arah_x = 0
            arah_y = 1

    # update
    uler.move(arah_x,arah_y)
    # render
    arena.render(10)

pygame.quit()

