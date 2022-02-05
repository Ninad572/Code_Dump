list1 = ["Stone", "Paper", "Scissor"]
import random
l=[1,2,3]
c = 0
b = 0
p = 0
while (c < 10):
    print(f"Round Number-{c + 1}")
    print("Please Enter A Valid Input Or Else You Will Be Removed From The Game")
    print("1)Stone.\n2)Paper.\n3)Scissor.")
    q = int(input("Enter Your Choice-"))
    a = random.choice(list1)
    print(a,"VS",list1[q-1])
    if q in l:
        if ((a == "Stone" and q == 3) or (a == "Scissor" and q == 2) or (a == "Paper" and q == 1)):
            print("Bot Won This Round! :( Better Luck Next Time.")
            b += 1
            c += 1
        elif ((a == "Stone" and q == 1) or (a == "Scissor" and q == 3) or (a == "Paper" and q == 2)):
            print("This Round Ended In a Draw.")
            c = c + 1
        else:
            print("Congratulations! You Won This Round.")
            p += 1
            c += 1
    else:
        print("Invalid Input!")
        break
print("Rounds Won By Bot--", b)
print("Rounds Won By You--", p)
print("Rounds Which Ended In A Draw--", (10 - (p + b)))
if (b > p):
    print("Bot Won The Game :(")
elif (p > b):
    print("Congratulations! You Won The Game.")
else:
    print("It's A Draw!")
