import numpy as np

ch1 = chr(66)
ch2 = chr(70)

alan = 3
usedMoves = np.empty((alan,alan), dtype='<U10')


class Player():
    def __init__(self,letter):
        self.letter = letter

def PrepareBoard():
    for i in range(0,alan):
        for j in range(0,alan):
            usedMoves[i][j] = "_"

def DrawBoard():
    # for i in range(0,alan):
    #     for j in range(0,alan):
    #         print(usedMoves[i][j])
    #         print("|")
    #     print("\n")
    print(usedMoves)

x = Player("X")
o = Player("O")

n = 0

def Sira(no=n):
    if no%2==0:
        return x
    else:
        return o

def Move():
    kontrol = True

    while(kontrol==True):
        print("Sira {}'in :\n".format(Sira().letter))
        movex = int(input("X koordinatini giriniz: "))
        movey = int(input("Y koordinatini giriniz: "))
        if(usedMoves[movex][movey]!="_"):
            print("Gecersiz konum. Lutfen Oynanmamis bir konum seciniz...")
        else:
            kontrol = False
        usedMoves[movex][movey] = Sira().letter
        
    global n
    n+=1

def Play():
    DrawBoard()
    Move()

def Column():
    for i in range(0,alan):
        for j in range(0,alan-1):
            if usedMoves[i][j]!=usedMoves[i][j+1]and(usedMoves[i][j]=="X" or usedMoves[i][j]=="O"):
                return False
        # print("Column")
        return True

def Row():
    for i in range(0,alan):
        for j in range(0,alan-1):
            if usedMoves[j][i]!=usedMoves[j+1][i]and(usedMoves[i][j]=="X" or usedMoves[i][j]=="O"):
                return False
        # print("Row")
        return True

def Diagonal1():
    for j in range(0,alan):
        for i in range(0,alan-1):
            if(usedMoves[i][i]!=usedMoves[i+1][i+1]):
                return False
    # print("Diagonal1")
    return True
def Diagonal2():
    for j in range(0,alan):
        for i in range(0,alan):
            if(usedMoves[alan-i-2][j]!=usedMoves[alan-i-1][j]):
                return False
    # print("Diagonal2")
    return True


def isOver():
    if (Column() or Row() or Diagonal1() or Diagonal2())and n!=0:
        if(n==alan*alan):
            print("Berabere kaldiniz..")    
        else:
            print("{} kazandi!".format(Sira(n-1).letter))
        return True
    return False

def main():
    PrepareBoard()
    while(isOver()==False):
        Play()
    DrawBoard()
    
    

main()
