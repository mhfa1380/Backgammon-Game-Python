import random
import os

game_board = []


def start_game():
    game = []
    for satr in range(0, 26):
        if satr == 1:
            game.append(['s', 's'])
        elif satr == 6:
            game.append(['a', 'a', 'a', 'a', 'a'])
        elif satr == 8:
            game.append(['a', 'a', 'a'])
        elif satr == 12:
            game.append(['s', 's', 's', 's', 's'])
        elif satr == 13:
            game.append(['a', 'a', 'a', 'a', 'a'])
        elif satr == 17:
            game.append(['s', 's', 's'])
        elif satr == 19:
            game.append(['s', 's', 's', 's', 's'])
        elif satr == 24:
            game.append(['a', 'a'])
        else:
            game.append([])
    return game


def role_dice():
    first, second = random.choice(
        [1, 2, 3, 4, 5, 6]), random.choice([1, 2, 3, 4, 5, 6])
    return first, second


def cheak_dice(x, y):
    if x == y and x != '-' and y != '-':
        return True
    return False


def print_board(board):
    maxim = 0
    for satr in board:
        maxim = max(maxim, len(satr))

    for satr in reversed(range(maxim)):
        for index, soton in enumerate(board):
            try:
                print('  '+soton[satr], end='  ')
            except:
                if index == 0 or index == 25:
                    print(end="  |  ")
                else:
                    print(end="  .  ")

        print()

    print(end="  ")
    for j in range(len(board)):

        if j > 9:
            print(j, end="   ")
        else:
            print(j, end="    ")


def eat_him(where, who):
    global game_board
    if game_board[where].count(who) == 1:
        del game_board[where][game_board[where].index(who)]
        if who == "s":
            game_board[0].append('s')
        else:
            game_board[-1].append('a')


def go_out(mv_fr, which):
    global game_board
    counter_rast = 0
    counter_chap = 0
    if len(game_board[0]) > 0 or len(game_board[-1]) > 0:
        return False

    for (counter, item) in enumerate(game_board[1:25]):
        if counter >= 12:
            counter_rast += item.count(which)
        else:
            counter_chap += item.count(which)

    if which == 'a' and counter_rast == 0 and counter_chap > 0:
        try:

            return True
        except:
            return False
    elif which == 's' and counter_rast > 0 and counter_chap == 0:
        try:

            return True
        except:
            return False

    return False


def can_go(where, who):
    global game_board
    if game_board[where].count(who) > 1 or where == 0 or where == 25:
        input("You can not go to house number " +
              str(where) + " - press enter to continue")
        return False
    return True


def first_elm(f1, f2, who):
    if cheak_dice(f1, f2):
        print(who, 'turn\n', "dice1 :", f1, " - dice2 :",
              f2, " - dice3 :", f1, " - dice4 :", f2)
        print_board(game_board)
        return f1, f1, f1, f1
    else:
        print(who, 'turn\n', "dice1 :", f1, " - dice2 :", f2)
        print_board(game_board)
        return f1, f2, -1, -1


def mines_gou_out(f1, f2, mv_f):
    if (f1 == 1 or f2 == 1) and mv_f == 24:
        return True, 1
    elif (f1 == 2 or f2 == 2) and mv_f == 23:
        return True, 2
    elif (f1 == 3 or f2 == 3) and mv_f == 22:
        return True, 3
    elif (f1 == 4 or f2 == 5) and mv_f == 21:
        return True, 4
    elif (f1 == 5 or f2 == 5) and mv_f == 20:
        return True, 5
    elif (f1 == 6 or f2 == 6) and mv_f == 19:
        return True, 6
    else:
        return False, 0


def mover(f1, f2, who):
    global game_board
    x, y, x1, y1 = first_elm(f1, f2, who)
    while True:
        try:
            b_from = int(input("\nPress -1 to skip your turn - Select from ?"))
            if b_from == -1:
                break
            if len(game_board[b_from]) == 0:
                input("\nNothing to Move - press enter to continue")
                os.system('cls')
                first_elm(f1, f2, who)
                continue
            ans, dic = mines_gou_out(x, y, b_from)
            if who == 'SEFID':
                if go_out(b_from, 's'):

                    if ans:
                        if dic == x:
                            x = 0
                        elif dic == x1:
                            x1 = 0
                        elif dic == y:
                            y = 0
                        elif dic == y1:
                            y1 = 0
                        del game_board[b_from][-1]
                        if cheak_dice(f1, f2):
                            os.system('cls')
                            print(who, 'turn\n', "dice1 :", x, " - dice2 :",
                                  y, " - dice3 :", x1, " - dice4 :", y1)
                            print_board(game_board)
                            if x == 0 and y == 0 and x1 == 0 and y1 == 0:
                                break
                        else:
                            os.system('cls')
                            print(who, 'turn\n', "dice1 :", x, " - dice2 :", y)
                            print_board(game_board)
                            if x == 0 and y == 0:
                                break
                        continue
            else:
                if go_out(b_from, 'a'):

                    if ans:
                        if dic == x:
                            x = 0
                        elif dic == x1:
                            x1 = 0
                        elif dic == y:
                            y = 0
                        elif dic == y1:
                            y1 = 0
                        del game_board[b_from][-1]
                        if cheak_dice(f1, f2):
                            os.system('cls')
                            print(who, 'turn\n', "dice1 :", x, " - dice2 :",
                                  y, " - dice3 :", x1, " - dice4 :", y1)
                            print_board(game_board)
                            if x == 0 and y == 0 and x1 == 0 and y1 == 0:
                                break
                        else:
                            os.system('cls')
                            print(who, 'turn\n', "dice1 :", x, " - dice2 :", y)
                            print_board(game_board)
                            if x == 0 and y == 0:
                                break
                        continue

            b_to = int(input("Press -1 to go back - move to ?"))
            if b_to == -1:
                continue
            if b_to != 25 or b_to != 0:
                if who == "Abi":
                    if len(game_board[-1]) > 0 and b_from != 25:
                        input(
                            "First Enter the 25 house pieces into the game. - press enter to continue")
                    else:
                        try:
                            if game_board[b_from][game_board[b_from].index('a')] == 'a':
                                if b_from - b_to == x and b_from - b_to != 0 and b_to - b_from < 0:
                                    if can_go(b_to, 's'):
                                        del game_board[b_from][game_board[b_from].index(
                                            'a')]
                                        game_board[b_to].append('a')
                                        if x1 == 0 or x1 == -1:
                                            x = 0
                                        else:
                                            x1 = 0
                                        eat_him(b_to, 's')
                                elif b_from - b_to == y and b_from - b_to != 0 and b_to - b_from < 0:
                                    if can_go(b_to, 's'):
                                        del game_board[b_from][game_board[b_from].index(
                                            'a')]
                                        game_board[b_to].append('a')
                                        if y1 == 0 or y1 == -1:
                                            y = 0
                                        else:
                                            y1 = 0
                                        eat_him(b_to, 's')
                                else:
                                    input(
                                        "Can You Count? - press enter to continue")

                        except:
                            input("Not Yours - press enter to continue")

                else:
                    if len(game_board[0]) > 0 and b_from != 0:
                        input(
                            "First Enter the 0 house pieces into the game. - press enter to continue")
                    else:
                        try:
                            if game_board[b_from][game_board[b_from].index('s')] == 's':
                                if b_to - b_from == x and b_to - b_from != 0 and b_to - b_from > 0:
                                    if can_go(b_to, 'a'):
                                        del game_board[b_from][game_board[b_from].index(
                                            's')]
                                        game_board[b_to].append('s')
                                        if x1 == 0 or x1 == -1:
                                            x = 0
                                        else:
                                            x1 = 0
                                        eat_him(b_to, 'a')
                                elif b_to - b_from == y and b_to - b_from != 0 and b_to - b_from > 0:
                                    if can_go(b_to, 'a'):
                                        del game_board[b_from][game_board[b_from].index(
                                            's')]
                                        game_board[b_to].append('s')
                                        if y1 == 0 or y1 == -1:
                                            y = 0
                                        else:
                                            y1 = 0
                                        eat_him(b_to, 'a')
                                else:
                                    input(
                                        "Can You Count? - press enter to continue")

                        except:
                            input("Not Yours - press enter to continue")

            else:
                input("Where are you going?")

            if cheak_dice(f1, f2):
                os.system('cls')
                print(who, 'turn\n', "dice1 :", x, " - dice2 :",
                      y, " - dice3 :", x1, " - dice4 :", y1)
                print_board(game_board)
                if x == 0 and y == 0 and x1 == 0 and y1 == 0:
                    break
            else:
                os.system('cls')
                print(who, 'turn\n', "dice1 :", x, " - dice2 :", y)
                print_board(game_board)
                if x == 0 and y == 0:
                    break
        except:
            print("Wrong input")
            os.system('cls')
            first_elm(f1, f2, who)


game_board = start_game()


while True:
    x, y = role_dice()
    input("\n\nSEFID Start!")
    os.system('cls')
    mover(x, y, 'SEFID')
    input("\n\nAbi Start!")
    x, y = role_dice()
    os.system('cls')
    mover(x, y, 'Abi')
