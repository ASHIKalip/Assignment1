import random
def calu(h):
    ci=random.randint(1,6)
    if(h<ci):
        print("you lost")
        print(ci,end="   ")
        print("This is comp number")
    elif(h==ci):
        print("correct guess keep going")
        i=int(input())
        calu(i)
    else:
        print("you won")
        print(ci,end="   ")
        print("This is comp number")
h=int(input())
if(h>6):
	print("NONE")
calu(h)
