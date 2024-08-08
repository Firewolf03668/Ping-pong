from pygame import *
import random
 




font.init()


win_width = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption("Ping pong")

background = transform.scale(image.load("pictire.jpg"),(700,500))
racket1 = "pingpong.png"
racket2 = "pingpong.png"
ball = "мяч.png"

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,height,width):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(self.height,self.width))
        self.rect = self.image.get_rect()        
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <  350:
            self.rect.y += self.speed

racket1 = Player(racket1, 30, 200, 4, 30, 150) 
racket2 = Player(racket2, 630, 200, 4, 30, 150)
ball = GameSprite(ball, 200, 200, 4, 50, 50)
 
 
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
 
speed_x = 3
speed_y = 3
finish = False
game = True
while game:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    if finish !=True:
        if finish != True:
            window.blit(background,(0,0))
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.y += speed_y
    
    
            if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
                speed_y *= 1
        
        #если мяч достигает границ экрана, меняем направление его движения
            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1
    
    
        #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (230, 230))
                game_over = True
    
    
        #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
            if ball.rect.x > 650:
                finish = True
                window.blit(lose2, (230, 230))
                game_over = True
    
    
        racket1.reset()
        racket2.reset()
        ball.reset()
    

           
    clock.tick(FPS)
    display.update()