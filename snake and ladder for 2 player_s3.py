# program to play snake and ladder
import random
s=0
m=0
while(s<=100 and m<=100):
    if(s==8):
        s=37
        print("ladder")
    elif(s==11):
        s=2
        print("snake")
    elif(s==13):
         s=34
         print("ladder")
    elif(s==25):
        s=4
        print("snake")
    elif(s==38):
        s=9
        print("snake")
    elif(s==40):
        s=68
        print("ladder")
    elif(s==52):
        s=81
        print("ladder")
    elif(s==65):
        s=46
        print("snake")
    elif(s==76):
        s=97
        print("ladder")
    elif(s==93):
        s=64
        print("snake")
    elif(s==100):
        print("player1 has won")
    elif(m==8):
        m=37
        print("ladder")
    elif(m==11):
        m=2
        print("snake")
    elif(m==13):
         m=34
         print("ladder")
    elif(m==25):
        m=4
        print("snake")
    elif(m==38):
        m=9
        print("snake")
    elif(m==40):
        m=68
        print("ladder")
    elif(m==52):
        m=81
        print("ladder")
    elif(m==65):
        m=46
        print("snake")
    elif(m==76):
        m=97
        print("ladder")
    elif(m==93):
        m=64
        print("snake")
    elif(m==100):
        print("player 2 has won")
    if(m>=100):
        print("try it again")
    if(s<=100 and m<=100):
        a=input("enter R or k")
        if(a=='r'):
            b=input("enter d to roll a dice for player1")
        if(b=='d'):
            d=random.randint(1,6)
            s=s+d
        elif(a=='k'):
                b=input("enter d to roll a dice for player2")
                if(b=='d'):
                    d=random.randint(1,6)
                    m=m+d
        else:
            print("invaild")
    else:
            print("try it again")
        
    print("the dice value",d)
    print("the present place p1ayer1",s)
    print("the present place p1ayer2",m)
