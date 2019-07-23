import numpy as np
import random
import matplotlib.pyplot as plt

plt.rcParams["patch.force_edgecolor"] = True  # to make edges in figure


class TicTac:

    def __init__(self):

        self.z = True

        self.board = self.create_plan()
        # self.player_num = self.get_player_num()

        self.player_num = 1
        self.pc_num = 2
        self.winner = False

        print("pc number is :", self.pc_num)

        self.player_1 = 0
        self.player_2 = 0

        while self.z and self.winner is False:
            self.play(self.player_num, self.pc_num)

        print("final play :\n", self.board)

        if self.winner == self.player_num:
            self.player_1 += 1
            self.winner_name = "YOU .... Congrats :D :D "
        if self.winner == self.pc_num:
            self.player_2 += 1
            self.winner_name = "Pc"
        try:
            print(f"the winner is {self.winner} : {self.winner_name}")
        except AttributeError:
            print(f"It's a {self.winner}")

    def create_plan(self):
        board = np.zeros((3, 3))
        return board

    def pc_choose(self, board, player):
        print("pc chose")
        bef_set_choose = board

        while np.array_equal(bef_set_choose, board):
            x = random.choice(range(3))
            y = random.choice(range(3))
            if board[x, y] == 0:
                board[x, y] = player
                return board
            elif np.all(board):
                return board

            else:
                pass



    def player_choose(self, board, player):
        bef_set_choose = board

        while np.array_equal(bef_set_choose, board):
            x = self.get_position()

            while x[0] > 2 or x[0] < 0 or x[1] > 2 or x[1] < 0:
                x = self.get_position()

            if board[x[0], x[1]] == 0:
                board[x[0], x[1]] = player
                return board
            else:
                print("used place")


    def get_winner(self, board):

        for i in range(3):
            x_hor = board[i][0] == board[i][1] == board[i][2] != 0
            if x_hor:
                self.winner = board[i][0]
                return self.winner, board

        for i in range(3):
            x_vir = board[0][i] == board[1][i] == board[2][i] != 0
            if x_vir:
                self.winner = board[0][i]
                return self.winner, board

        if np.all(np.diag(board) == self.player_num) or np.all(np.diag(board) == self.pc_num):
            self.winner = np.diag(board)[0]
            return self.winner, board

        if np.all(np.diag(np.fliplr(board)) == self.player_num) or np.all(np.diag(np.fliplr(board)) == self.pc_num):
            self.winner = np.diag(np.fliplr(board))[0]
            return self.winner, board

        if np.all(board):
            self.z = False
            self.winner = " Withdraw "
            return self.winner, board

        return self.winner

    def play(self, player_num, pc_num):

        self.pc_choose(self.board, player_num)
        if self.get_winner(self.board):
            return self.get_winner(self.board)

        self.pc_choose(self.board, pc_num)
        if self.get_winner(self.board):
            return self.get_winner(self.board)

        return


player_1 = 0
player_2 = 0

x = 100

for i in range(x):
    game = TicTac()
    player_1 += game.player_1
    player_2 += game.player_2


withdraw_in_game = (x-player_1-player_2)

print("player_1 : ", player_1)

print("player_2 : ", player_2)

print("withdraw_in_game :", withdraw_in_game)

plt.plot([1, 1], [0, player_1], "-k", label=f'player one {player_1}')

plt.plot([2, 2], [0, player_2], "-r", label=f"player two {player_2}")

plt.plot([3, 3], [0, withdraw_in_game], "-m",
         linewidth=1, markersize=4, label=f"withdraw val in game {withdraw_in_game}")


plt.legend()

plt.axis([0, 4, 0, 100])

plt.show()

