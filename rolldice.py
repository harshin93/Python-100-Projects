import random
count1 = 0
count2 = 0
count3 = 0
def dice():
    player1_list = [1,2,3,4,5,6]
    player2_list = [1,2,3,4,5,6]

    player1 = random.choice(player1_list)
#     print('player 1: ',player1)
    player2 = random.choice(player2_list)
#     print('player 2: ',player2)

    global count1, count2, count3
    
    if player1 > player2:
#         print("Player 1 won")
        count1 = count1 + 1
    elif player1 < player2:
#         print("PLayer 2 won")
        count2 = count2 + 1
    else:
#         print("TIE")
        count3 = count3 + 1
def repeat(times, f):
    for i in range(times):
        f()
    print('player 1 has won ', count1, ' times')
    print('player 2 has won ', count2, ' times')
    print('Tie has occur ', count3,  ' times')
if __name__ == "__main__":
    repeat(100000, dice)