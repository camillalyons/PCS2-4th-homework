#SKETCH OF THE PROGRAM

def game (n1, n2, n3, n4):
    if n1 <= 3:
        n1 = 0
    if n2 <= 0:
        n2 = 0
    if n3 <= 3:
        n3 = 0
    if n4 <= 3:
        n4 = 0

    tot = n1+n2+n3+n4
    vals = []    #this list will contain all the numbers different from 0
    if n1 != 0:
        vals.append(n1)
    if n2 != 0:
        vals.append(n2)
    if n3 != 0:
        vals.append(n3)
    if n4 != 0:
        vals.append(n4)

    if tot % 3 == 0:
        print ("sorry, can't win")

    if tot % 3 == 1:    #the generic case in which the sum is a multiple of 3+1
        minval = min(vals)
        if n1 == minval:
            n1 -= 1
        if n2 == minval:
            n2 -= 1
        if n3 == minval:
            n3 -= 1
        if n4 == minval:
            n4 -= 1
    if tot % 3 == 2:
        #the 4x4 exception
        if n1 and (n2+n3+n4) == 4:
            n1 -= 1
            n2-= 2
        if n2 and (n1+n3+n4) == 4:
            n2 -= 1
            n3 -= 1
        if n3 and (n1+n2+n4) == 4:
            n3 -= 1
            n4 -= 1
        if n4 and (n1+n2+n3) == 4:
            n4 -= 1
            n1 -= 1
        #the generic case in which the sum is a multiple of 3 + 2
        maxval = max(vals)
        if n1 == maxval:
            n1 -= 2
        if n2 == maxval:
            n2 -= 2
        if n3 == maxval:
            n3 -= 2
        if n4 == maxval:
            n4 -= 2
    return (n1,n2,n3,n4)

def recursivegame(n1,n2,n3,n4):
    if n1+n2+n3 or n1+n2+n4 or n1+n3+n4 or n2+n3+n4 == 0:    #if there are at least 3 zeros, so we are left with inly 1 bases, so we have won
        condition = True
        print ('hurray!')
    else:
        condition = False
    while condition == False:
        game(n1,n2,n3,n4)




