import random
import sys
class ProblemSolver:
    def faltaanos(self,nome, idade, times):
        print("Ola "+nome)
        for x in times:
                print("Fique sabendo "+nome," ")
                print(100-idade," ")
                print("E a quantia de tempo que lhe falta para os 100 anos.")

    def evenorodd(self, number, check):
        if number%4==0:
            print("Your number is divisible by 2^2")
        elif number%2==0: 
            print("Your number is divisible by 2^1")
        else:
            print("Your number is quite odd.")
        if number%check==0:
            print("Your number is divisible by the second number")
        else:
            print("Your number is not divisible by the second number.")

    def takelist(self,number):
        a=[]
        b=[]
        for i in 20:
            if i==0:
                a[i]=1
            elif i==1:
                a[i]=1
            else:
                a[i]=a[i-1]+a[i-2]
            if number==true:
                for x in a:
                    if a[x]<number:
                        b[x]=a[x]
                print(b)
            else:
                for x in a:
                    if a[x]<5:
                        b[x]=a[x]
                print(b)
            
    def comparelist(self):
        a=[]
        print("This is list A"+str(a))
        b=[]
        print("This is list B"+str(b))
        c=random.randint(5,20)
        d=random.randint(10,25)
        for i in c:
            if i==0:
                a[i]=1
            elif i==1:
                a[i]=1
            else:
                a[i]=a[i-1]+a[i-2]
        for x in d:
            b[x]=x%c
            e=[]
        for y in a:
            for z in b:
                if a[y]==b[z]:
                     e.insert(-1,a[y])
            print(e)

    def tryagainkiddo(self,numbah,attempt):
        if numbah==attempt:
            print("Well done! Now type exit to stop the game.")
        else:
            print("Try again Kiddo")
        
    def guessmynumba(self):
        numbah=randint(1,9)
        while(attempt!="exit"):
            attempt=input("Type any number.")
            tryagainkiddo(numbah,attempt)
