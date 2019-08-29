from random import randint
a1='1'
a2='2'
a3='3'
a4='4'
a5='5'
a6='6'
a7='7'
a8='8'
a9='9'
i=1
def tic():
    print('       |       |       ')
    print('   ' + a7 + '   |   ' + a8 + '   |   ' + a9)
    print('       |       |       ')
    print('________________________')
    print('       |       |       ')
    print('   ' + a4 + '   |   ' + a5 + '   |   ' + a6)
    print('       |       |       ')
    print('________________________')
    print('       |       |       ')
    print('   ' + a1 + '   |   ' + a2 + '   |   ' + a3)
    print('       |       |       ')
def check_position():
    if a1=='O' or a1=='X':
        print('u played wrong')
                  
def cross():
    print('select above no. for marking cross')
    n = input()
    check_position()
    if n == '1':
        global a1
        a1='X'
        tic()
    elif n == '2':
        global a2
        a2 = 'X'
        tic()
    elif n == '3':
        global a3
        a3 = 'X'
        tic()
    elif n == '4':
        global a4
        a4 = 'X'
        tic()
    elif n == '5':
        global a5
        a5 = 'X'
        tic()
    elif n == '6':
        global a6
        a6 = 'X'
        tic()
    elif n == '7':
        global a7
        a7 = 'X'
        tic()
    elif n == '8':
        global a8
        a8 = 'X'
        tic()
    elif n == '9':
        global a9
        a9 = 'X'
        tic()
    else:
        print('please select above numbers only')
def circle():
    
    print('select above no. for marking circle')
    n = input()
    if n == '1':
        global a1
        a1 = 'O'
        tic()
    elif n == '2':
        global a2
        a2 = 'O'
        tic()
    elif n == '3':
        global a3
        a3 = 'O'
        tic()
    elif n == '4':
        global a4
        a4 = 'O'
        tic()
    elif n == '5':
        global a5
        a5 = 'O'
        tic()
    elif n == '6':
        global a6
        a6 = 'O'
        tic()
    elif n == '7':
        global a7
        a7 = 'O'
        tic()
    elif n == '8':
        global a8
        a8 = 'O'
        tic()
    elif n == '9':
        global a9
        a9 = 'O'
        tic()
    else:
        print('please select above numbers only')
def check():
    if a1==a2==a3=='X' or a1==a4==a7=='X' or a1==a5==a9=='X'or a2==a5==a8=='X'or a3==a6==a9=='X' or a3==a5==a7=='X' or a4==a5==a6=='X' or a7==a8==a9=='X':
        print("X won the game")
       # replay()
        quit()
    elif a1==a2==a3=='O' or a1==a4==a7=='O' or a1==a5==a9=='O'or a2==a5==a8=='O' or a3==a6==a9=='O' or a3==a5==a7=='O' or a4==a5==a6=='O'or a7==a8==a9=='O':
        print('O wins the game')
       # replay()
        quit()
def choose_first():
    if randint(0,1)==0:
        print('player 1 goes first')
    else:
        print('player 2 goes first')
        
'''
def replay():
    return input('do you want to play again?....yes or no').lower.startswith('y')    
'''

tic()
choose_first()
for no in range(0,5):
    cross()
    check()
    circle()
    check()
    
print('it is a draw')
quit()


