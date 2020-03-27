user=int(input("0->Rock, 1->Paper, 2->scissors"))
import random
comp= random.randint(0,2)
if user==0 and comp==1:
    print("user:",user,"comp",comp,"Cpu Wins")
elif user==1 and comp==2:
    print("user:",user,"comp",comp,"Cpu Wins")
elif user==2 and comp==0:
    print("user:",user,"comp",comp,"Cpu Wins")
elif user==comp:
    print("user:",user,"comp",comp,"tie")
else:
    print("user:",user,"comp",comp,"Player Wins")
    
