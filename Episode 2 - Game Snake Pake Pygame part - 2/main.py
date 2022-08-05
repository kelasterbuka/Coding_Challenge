import pygame
from Game import Arena,Uler,Mamam

# initialisasi game
# arena
arena = Arena(500,500,20,20)
# object game
uler = Uler(arena,(10,10),arah_x=1)
mamam = Mamam(arena,nama="mamam")

# aplikasi sama rendering time
isRun = True
tick = 10

while isRun:
    # user window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # update
    uler.move()

    if uler.is_collide():
        arena.reset_member()
        uler.reset()
        mamam = Mamam(arena,nama="mamam")

    if uler.get_pos() == mamam.get_pos():
        uler.tambah_kotak()
        mamam.ubah_pos()

    # render
    arena.render(tick)

pygame.quit()