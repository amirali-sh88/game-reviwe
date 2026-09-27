import os
from dotenv import load_detenv
from question import questions


load_detenv()
admin_password =os.getenv("quiz_admin_password")
open_admin=input("do u wnt to open admin mode?  yes/no")


if open_admin.lower()=="yes":
    enter_pass =input("enter admin password")
    if enter_pass==admin_password:
        print("admin hi")
    else:
        print("wrong pass")

name = input("what is your name? ")

if name:
    print("correct")
else:
    print("wrong")

game = input("game name: ")

if game:
    print("correct")
else:
    print("wrong")

score = input("rate this game from 1 to 5: ")

if score in ["1", "2", "3", "4", "5"]:
    print("correct")
else:
    print("wrong")
print("please enter a number from 1 to 5")
score = input("rate this game from 1 to 5: ")

review = input("write a short review: ")

if review:
    print("correct")
else:
    print("wrong")

with open("game_reviews.txt", "a") as file:
    file.write(name + " - " + game + " - " + score + "/5 - " + review + "\n")

print("your review was saved")
