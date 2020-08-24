import random

if __name__ == "__main__":

    dic = {0:'rock',1:'spock',2:'paper',3:'lizard',4:'scissors',}

    player = random.randint(0,4)
    com = random.randint(0,4)

    print('Player chooses %s' % dic.get(player))
    print('Computer chooses %s' % dic.get(com))

    if player == com:
        print('draw')
        quit()
    if player>=2:
        loser = [player-1, player-2]
    else:
        # Iterate over the whole array i.e. 0 -> [4, 3]
        loser = [5-player-1, 5-player-2]

    if com in loser:
        print("Player wins!")
    else:
        print('Computer win!')
