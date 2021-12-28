import random
#TEST!
field2=[[' ','1','2','3'],['1',' ',' ',' '],['2',' ',' ',' '],['3',' ',' ',' ']]


def printfield(field):
    for i in range (0,len(field)):
        st =''
        for j in range (0,len(field[0])):
            st+=field[i][j]
        print (st)

def fullfield(field):
    res=True
    for i in range (1,len(field)):
        for j in range (1,len(field[0])):
            if field[i][j]==' ':
                res=False
                break
    return res

def checkwin(field,sym):
    r1=(field[1][1]==sym)and(field[2][1]==sym)and(field[3][1]==sym)
    r2=(field[1][1]==sym)and(field[1][2]==sym)and(field[1][3]==sym)
    r3=(field[1][3]==sym)and(field[2][3]==sym)and(field[3][3]==sym)
    r4=(field[3][1]==sym)and(field[3][2]==sym)and(field[3][3]==sym)
    r5=(field[1][1]==sym)and(field[2][2]==sym)and(field[3][3]==sym)
    r6=(field[1][3]==sym)and(field[2][2]==sym)and(field[3][1]==sym)
    r7=(field[1][2]==sym)and(field[2][2]==sym)and(field[3][2]==sym)
    r8=(field[2][1]==sym)and(field[2][2]==sym)and(field[2][3]==sym)
    res=r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8
    return res



answ=input('Сыграем в "Крестики-нолики?" (y/n)')
if answ=='y':
    printfield(field2)
    first=random.randint(0, 1)

    if first ==0:
        print('Первый ход мой, я играю крестиками')
    else:
        print('Первый ход твой, ты играешь крестиками')
    move=first
    if first==0:
        user='o'
        comp='x'
    else:
        user='x'
        comp='o'
    iswinner=False    
    while fullfield(field2)==False:
        if move==0:
            x=0
            y=0
            x=random.randint(1, 3)
            y=random.randint(1, 3)
            while field2[y][x]!=' ':
                x=random.randint(1, 3)
                y=random.randint(1, 3)
            field2[y][x]=comp
            if checkwin(field2,comp):
                printfield(field2)
                print ('Я выиграл за ',comp,'!')
                iswinner=True
                break
            move=1
        else:
            x=int(input('№ столбца:'))
            y=int(input('№ строки:'))
            while field2[y][x]!=' ':
                print('Клетка занята, повтори ход!')
                x=int(input('№ столбца:'))
                y=int(input('№ строки:'))
            field2[y][x]=user
            if checkwin(field2,user):
                printfield(field2)
                print ('Ты выиграл за ',user,'!')
                iswinner=True
                break
            move=0
        printfield(field2)
    if iswinner==False:
        print('Ничья!')
    print('КОНЕЦ ИГРЫ!!!')
else:
    print('Ну как хочешь! Пока...')
