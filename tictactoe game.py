# take player name to identify
playerA = input("player A - write your name here ")
playerB = input("player B - write your name here ")

boardgame = {
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'G1': ' ', 'G2': ' ', 'G3': ' ',
    'P1': ' ', 'P2': ' ', 'P3': ' '
}

player = 1 # to initialise player A
total_moves = 0 # to count the moves
endgame = 0

def check():
    if boardgame['B1'] == 'X' and boardgame['B2'] == 'X' and boardgame['B3'] == 'X':
        print(playerA, " Won!")
        return 1
    if boardgame['G1'] == 'X' and boardgame['G2'] == 'X' and boardgame['G3'] == 'X':
        print(playerA, " Won!")
        return 1
    if boardgame['P1'] == 'X' and boardgame['P2'] == 'X' and boardgame['P3'] == 'X':
        print(playerA, " Won!")
        return 1 #horizontal check
    if boardgame['B1'] == 'X' and boardgame['G2'] == 'X' and boardgame['P3'] == 'X':
        print(playerA, " Won!")
        return 1
    if boardgame['B3'] == 'X' and boardgame['G2'] == 'X' and boardgame['P1'] == 'X':
        print(playerA, " Won!")
        return 1 # vertical check
    if boardgame['B1'] == 'X' and boardgame['G1'] == 'X' and boardgame['P1'] == 'X':
        print(playerA, " Won!")
        return 1
    if boardgame['B2'] == 'X' and boardgame['G2'] == 'X' and boardgame['P2'] == 'X':
        print(playerA, " Won!")
        return 1
    if boardgame['B3'] == 'X' and boardgame['G3'] == 'X' and boardgame['P3'] == 'X':
        print(playerA, " Won!")
        return 1 #vertital check

    # PLAYER TWO
    if boardgame['B1'] == 'O' and boardgame['B2'] == 'O' and boardgame['B3'] == 'O':
        print(playerB, " Won!")
        return 1
    if boardgame['G1'] == 'O' and boardgame['G2'] == 'O' and boardgame['G3'] == 'O':
        print(playerB, " Won!")
        return 1
    if boardgame['P1'] == 'O' and boardgame['P2'] == 'O' and boardgame['P3'] == 'O':
        print(playerB, " Won!")
        return 1 #horizontal check
    if boardgame['B1'] == 'O' and boardgame['G2'] == 'O' and boardgame['P3'] == 'O':
        print(playerB, " Won!")
        return 1
    if boardgame['B3'] == 'O' and boardgame['G2'] == 'O' and boardgame['P1'] == 'O':
        print(playerB, " Won!")
        return 1 # vertical check
    if boardgame['B1'] == 'O' and boardgame['G1'] == 'O' and boardgame['P1'] == 'O':
        print(playerB, " Won!")
        return 1
    if boardgame['B2'] == 'O' and boardgame['G2'] == 'O' and boardgame['P2'] == 'O':
        print(playerB, " Won!")
        return 1
    if boardgame['B3'] == 'O' and boardgame['G3'] == 'O' and boardgame['P3'] == 'O':
        print(playerB, " Won!")
        return 1 #vertital check
    return 0
    
    

print('B1|B2|B3')
print('- +- +-')
print('G1|G2|G3')
print('- +- +-')
print('P1|P2|P3')
print('************************************')

while True:
    print(boardgame['B1'] + '|' + boardgame['B2'] + '|' + boardgame['B3'])
    print('-+-+-')
    print(boardgame['G1'] + '|' + boardgame['G2'] + '|' + boardgame['G3'])
    print('-+-+-')
    print(boardgame['P1'] + '|' + boardgame['P2'] + '|' + boardgame['P3'])
    endgame = check()
    if total_moves == 9 or endgame == 1:
        break
    while True:
        if player == 1:
            play1 = input(playerA + ' Your Turn')
            if play1.upper() in boardgame and boardgame[play1.upper()] == ' ':
                boardgame[play1.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid input, Please Try Again ;-)')
                continue
        else:
            play2 = input(playerB + ' Your Trun')
            if play2.upper() in boardgame and boardgame[play2.upper()] == ' ':
                boardgame[play2.upper()] = 'O'
                player = 1
                break
            else:
                print('Invalid Input, Please Try Again')
                continue
    total_moves += 1
    
