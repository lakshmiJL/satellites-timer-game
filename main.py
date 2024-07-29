import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
no_of_sats = 10
sats = []
next = 0 #index for the satellite list
lines = []

start= time()
end = 0
total = 0
#print(start)

for i in range(no_of_sats):
    satellite = Actor("satellite")
    satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
    sats.append(satellite)
print(sats)


def draw():
    global total
    screen.blit("background",(0,0))
    number = 1
    for satellite in sats:
        satellite.draw()
        screen.draw.text(str(number),(satellite.x,satellite.y-25))
        number = number + 1
    if next < no_of_sats and total <= 15:
        total = time() - start
        total = round(total,1)
        screen.draw.text(str(total),(50,50))
    else:
        screen.draw.text(str(total),(50,50))
    for line in lines:
        screen.draw.line(line[0],line[1],color="white")
def update():
    pass
def on_mouse_down(pos):
    global next, total, lines
    if next< no_of_sats and total<= 15:
        if sats[next].collidepoint(pos):
            if next:
                lines.append((sats[next-1].pos,sats[next].pos))
                print(lines)
            next += 1
        else:
            lines = []
            next = 0
        
pgzrun.go()
