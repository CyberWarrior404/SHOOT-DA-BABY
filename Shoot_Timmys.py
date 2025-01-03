import pgzrun


WIDTH=600
HEIGHT=450

bullets = []

Gun = Actor("gun.png")
Gun.x=WIDTH/2
Gun.y=HEIGHT-110
def draw():
    screen.blit("space_bg.jpg",(0,0))
    Gun.draw() 

def update():
    if keyboard.left:
        Gun.x-=2
    elif keyboard.right:
       Gun.x+=2

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullets"))
        bullets[-1].x=Gun.x
        bullets[-1].y=Gun.y-40


pgzrun.go()