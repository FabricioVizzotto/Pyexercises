import random
import sys
class ProblemSolver:
    
    def faltaanos(self, nome, idade, times):
        print("Ola "+nome)
        for x in range(times):
            print("Fique sabendo "+nome)
            print(100-idade)
            print("E a quantia de tempo que lhe falta para os 100 anos.")

    def evenorodd(self, number, check):
        print("metodo 2: ")
        if number%4 == 0:
            print("Your number is divisible by 2^2")
        elif number%2 == 0:
            print("Your number is divisible by 2^1")
        else:
            print("Your number is quite odd.")
        if number%check == 0:
            print("Your number is divisible by the second number")
        else:
            print("Your number is not divisible by the second number.")

    def takelist(self, number):
        print("metodo 3: ")
        a = [0] * 20
        b = []
        for i in range(20):
            if i == 0:
                a[i] = 1
            elif i == 1:
                a[i] = 1
            else:
                a[i] = a[i-1] + a[i-2]
        if number:
            for x in range(20):
                if a[x] <= number:
                    b.append(a[x])
        else:
            for x in range(20):
                if a[x] <= 5:
                    b.append(a[x])
        print(b)

    def comparelist(self):
        print("metodo 4")
        c=random.randint(5, 20)
        d=random.randint(10, 25)
        a = [0] * c
        b = [0] * d
        for i in range(c):
            if i == 0:
                a[i] = 1
            elif i == 1:
                a[i] = 1
            else:
                a[i] = a[i-1] + a[i-2]
        print(a)
        for x in range(d):
            b[x] = x%c
        print(b)
        e = []
        for y in range(c):
            for z in range(d):
                if a[y] == b[z]:
                     e.append(a[y])
        print(e)

    def guessmynumba(self):
        print("metodo 5")
        attempt = ""
        numbah = random.randint(1,9)
        i = 1
        while(i):
            attempt = input("Type your number: ")
            if attempt == exit:
                print("bye")
                i -= 1
            else:
                if int(attempt) < numbah:
                    print("Your number is smaller than rand.")
                elif int(attempt) > numbah:
                    print("Your number is bigger than rand.")
                elif int(attempt) == numbah:
                    print("Yes! You did it! Now type exit to end game.")
                else:
                    print("Didn't you type a number ?")
