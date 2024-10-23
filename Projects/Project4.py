# Beginning: create variables
extrovert_points = 0
introvert_points = 0
ambivert_points = 0

# Middle: Ask questions
#question 1: 
answer = input("On a weekend would you rather A) hangout with friends, or B) watch a movie by yourself,or C) do homework with a friend?")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1 
elif answer == "C"
        ambivert_points += 1

# question 2:
answer = input(" Eat lunch with a group A,)eat by yourself,B) or C) eat with one other person")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1
elif answer == "C":
        ambivert_points += 1

# question 3:
answer = input("Would you go to the mall with a lot of friends, A) or B) window shop,or C) go to the mall with your mom?")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1
elif answer == "C":
        ambivert_points += 1
# question 4:
answer = input("Would you rather A) Do homework with your friend, B) do it by yourself, or C) have one of your parents help you/")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1
elif answer == "C":
        ambivert_points += 1

# question 5:
answer = input("Would you A) talk in front of a big crowd, B) talk in front of 20 people, or C) just talk to your parents?")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        ambivert_points += 1
elif answer == "C":
        introvert_points += 1

# End: determine results
if extrovert_points > introvert_points and > ambivert_points:
        print("You are an extrovert!")
elif introvert_points > extrovert_points and > ambivert_points:
        print("You are an introvert!")

elif ambivert_points > extrovert_points and > introvert_points:
        print("You are an ambivert!")

