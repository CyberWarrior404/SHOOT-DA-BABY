import pgzrun


WIDTH=600
HEIGHT=450

bullets = []
enemies = []

for x in range(10):
    for y in range(3):
        enemies.append(Actor("timmy.png"))
        enemies[-1].x=100+20*x
        enemies[-1].y=69+20*y

Gun = Actor("gun.png")
Gun.x=WIDTH/2
Gun.y=HEIGHT-110
def draw():
    screen.blit("space_bg.jpg",(0,0))
    Gun.draw() 
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

def update():
    if keyboard.left:
        Gun.x-=2
    elif keyboard.right:
       Gun.x+=2
    for bullet in bullets:
        if bullet.y <= -20:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    for enemy in enemies:
        enemy.y += 1


def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullets.png"))
        bullets[-1].x=Gun.x
        bullets[-1].y=Gun.y-40


pgzrun.go()