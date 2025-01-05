from pygame import *
from random import randint

#музыка
#mixer.init()
#mixer.music.load('')
#mixer.music.play()

#текст
font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 25)
win_text = font1.render('Вы выиграли!', 1,(255,255,255))
lose_text = font1.render('Вы проиграли!', 1,(180,0,0))
life = 9
lost = 0
score = 0

#файлы переменные
hero = 'cat.png'
enemy = 'dog.jpg'
fish = 'Fish.png'

#классы
class Game_Sprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_speed, size_x, size_y, sprite_x, sprite_y):
        sprite.Sprite().__init__()
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Cat(Game_Sprite):
    def run(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]  and self.rect.y <= 495:
            self.rect.y += self.speed

class Dog(Game_Sprite):
    def run(self):
        self.rect.x -= self.speed
        if self.rect.x >= 5:
            self.rect.y = randint(80, 420)
            self.rect.x = 700

class Fish(Game_Sprite):
    def run(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.x >= 5:
            self.rect.y = randint(80, 420)
            self.rect.x = 700
            lost += 1

#окно
window = display.set_mode((700, 500))
display.set_caption('Cat_game')
background = transform.scale(image.load('fon.jpg'), (700, 500))
window.blit(background, (0,0))

#создание спрайтов
kitty = Cat(hero, 10, 55, 35, 15, 5)

#dogs = sprite.Group()
#for i in range(1,6):
doggy = Dog(enemy, randint(5,20), 60, 30, 680, randint(5, 480))
    #dogs.add(doggy)

#fishes = sprite.Group()
#for i in range(1,3):
yummy = Fish(fish, randint(5,15), 35, 20, 680, randint(5,480))
    #fishes.add(yummy)

#игровой цикл
game = True
finish = False
a = time.Clock()
FPS = 60
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.blit(background, (0,0))
         #text
        life_text = font2.render('Жизни:'+ str(life), 1, (0,0,0))
        window.blit(life_text, (20,0))
        lost_text = font2.render('Пропущено:'+ str(lost), 1, (0,0,0))
        window.blit(lost_text, (50, 0))
        score_text = font2.render('Счёт:'+str(score), 1, (0,0,0))
        window.blit(score_text, (80,0))

         #
        kitty.reset()
        doggy.reset()
        yummy.reset()
         #
        kitty.run()
        doggy.run()
        yummy.run()

         #collide
        #collides = sprite.groupcollide(doggy, yummy, True, True)
        if sprite.spritecollide(kitty, doggy, False) or life <= 0 or lost == 10:
            window.blit(lose_text, (200, 200))
            finish = True
        
        if sprite.spritecollide(yummy, kitty, False):
            score += 1

        if score == 15:
            window.blit(win_text, (200, 200))
            finish = True
        
    display.update()
    a.tick(FPS)