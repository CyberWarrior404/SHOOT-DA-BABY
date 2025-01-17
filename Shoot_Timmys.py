import pgzrun


WIDTH=600
HEIGHT=450

bullets = []
enemies = []

for x in range(10):
    for y in range(3):
        enemies.append(Actor("timmy.png"))
        enemies[-1].x=100+40*x
        enemies[-1].y=69+40*y
    
direction = 1
score = 0
def draw_score():
    screen.draw.text(str(score),(100, 100))

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
    draw_score()

def update():
    global direction,score
    if keyboard.left:
        Gun.x-=2
    elif keyboard.right:
       Gun.x+=2
    for bullet in bullets:
        bullet.y -= 10
        if bullet.y<=-20:
            bullets.remove(bullet)
    move_down=False
    if len(enemies)>0 and (enemies[-1].x>WIDTH-20 or enemies[0].x<20):
        move_down=True
        direction=direction*-1
    for enemy in enemies:
        enemy.x+=2*direction
        if move_down==True:
            enemy.y+=5
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score+=1
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                break


def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullets.png"))
        bullets[-1].x=Gun.x
        bullets[-1].y=Gun.y-40


pgzrun.go()