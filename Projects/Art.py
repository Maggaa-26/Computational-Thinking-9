#start
import turtle, random, math

t = turtle.Turtle()
#comment
turtle.bgcolor("white")
t.speed(60)

colors = ["red","pink","gold"]
angles = [80,127]
sides =  [22, 14,10]
#comment
for i in range(15000):
    t.color( colors[i%3])
    t.forward(random.choice([22,14,10]))
    t.left(120)
