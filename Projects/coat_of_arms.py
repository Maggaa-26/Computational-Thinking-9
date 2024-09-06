###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("summer")

q1 = codesters.Square (100, 100, 200, 'orchid')
q2 = codesters.Square (-100, 100, 200, 'violet')
q3 = codesters.Square (-100, -100, 200, 'plum')
q4 = codesters.Square (100, -100, 200, 'thistle')

s1 = codesters.Sprite("dog", 100, 100)
s2 = codesters.Sprite("Volleyball.png", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite ("Shepherd.png", 100, -100)
s3.set_size(0.5)
# s4 = codesters.Sprite ("flowers.gif", -100, 100)
# s4.set_size(0.1)

# message1 = codesters.Text("Maggie Rettenmier",0,220,"black")
# message2 = codesters.Text("Burgers and delicious",0,-220,"black")