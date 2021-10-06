from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
click = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
handx = random.randrange(0,1281)
handy = random.randrange(0,1025)
while running:
    clear_canvas()
    if click == True:
        handx = random.randrange(0,1281)
        handy = random.randrange(0,1025)
        click = False
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(handx,handy)
    if handx <x:
        x-= 0.5
    elif handx >x:
        x += 0.5
    if handy<y:
        y-= 0.5
    elif handy>y:
        y+= 0.5
    if handx== x and handy==y:
        click = True
    update_canvas()
    frame = (frame + 1) % 8

    

close_canvas()




