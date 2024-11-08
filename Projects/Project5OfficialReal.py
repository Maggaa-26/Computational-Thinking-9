# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("spring.png")


player = codesters.Sprite("flower.gif")
player.set_size(0.4)
player.go_to(0,-200)
stage.disable_floor()

gameOver = False
count = 0


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("BEE.png", x_position, 250)
        object.set_size(0.2)
        object.set_y_speed(0.4)
   
stage.event_interval(falling_object,5.0)


# Section 3 - Collision


def collision(s1, s2):
    global count, gameOver
   
    if s2.get_image_name() == "BEE.png":
        stage.remove_sprite(s2)
        if count == 5:
            print("Game Over!") 
            gameOver = True
            player.say("Game over")
        else:
            print("Almost over")
            player.say("Almost over")
            count += 1


player.event_collision(collision)
def move_up(sprite):
    sprite.move_up(3)
     
def move_down(sprite):
    sprite.move_down(3)
    
def move_left(sprite):
    sprite.move_left(3)
    
def move_right(sprite):    
    sprite.move_right(3)
def forward (sprite):
    sprite.forward(3)


# Section 4 - Controls
player.event_key("up", move_up)
player.event_key("down", move_down)
player.event_key("left", move_left)
player.event_key("right", move_right)
player.event_key("i", forward)









