# -*- coding: utf-8 -*-
#/src/helpers/Game.py
"""
                         Tic-Toc-Toe
    ------------------------------------------------------------------------
                         Game
    ------------------------------------------------------------------------
"""
import random

class Game:
    """Game Tic-Toc-Toe

    This object will manage all the functions of the game
    """
    default_matrix = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
    default_round_game = 0

    def __init__(self, matrix = None, round_game = None, player = None):
        """init constructor
        """
        self.players = ['X', 'O']
        self.player = self.sort_player(player)
        self.matrix = self.set_matrix(matrix)
        self.round_game = self.set_round_game(round_game)

    def sort_player(self, player):
        """Sets the starting player"""
        if not player:
            return random.choice(self.players)
        return player

    def set_matrix(self, matrix):
        """Defines the matrix"""
        if not matrix:
            return self.default_matrix
        return matrix

    def set_round_game(self, round_game):
        """Sets the number of the move"""
        if not round_game:
            return self.default_round_game
        return round_game

    def rotate_matrix(self, mat):
        """Rotate matrix 90 degrees"""
        N=3
        for x in range(0, int(N / 2)):
            for y in range(x, N-x-1):
                temp = mat[x][y]
                mat[x][y] = mat[y][N-1-x]
                mat[y][N-1-x] = mat[N-1-x][N-1-y]
                mat[N-1-x][N-1-y] = mat[N-1-y][x]
                mat[N-1-y][x] = temp
        return mat

    def set_movement(self, x, y):
        """Performs the player's movement on the board"""
        if x < 0 or x > 2:
            return False
        if y < 0 or y > 2:
            return False
        rotation_one = self.rotate_matrix(self.matrix)
        rotation_two = self.rotate_matrix(rotation_one)
        matrix = self.rotate_matrix(rotation_two)
        if matrix[x][y] == " ":
            matrix[x][y] = self.player
            self.rotate_matrix = self.rotate_matrix(matrix)
            self.round_game = self.round_game + 1
            if self.player == self.players[0]:
                self.player = self.players[1]
            else:
                self.player = self.players[0]
            return True
        return False

    def check_game_over(self):
        """Checks match status"""
        #check lines
        for i in range(3):
            sum_mark_player_one = 0
            sum_mark_player_two = 0
            for j in range(3):
                if self.matrix[i][j] == self.players[0]:
                    sum_mark_player_one += 1
                if self.matrix[i][j] == self.players[1]:
                    sum_mark_player_two += 1
            if sum_mark_player_one == 3:
                return self.players[0]
            if sum_mark_player_two == 3:
                return self.players[1]
        #check colums
        for i in range(3):
            sum_mark_player_one = 0
            sum_mark_player_two = 0
            for j in range(3):
                if self.matrix[j][i] == self.players[0]:
                    sum_mark_player_one += 1
                if self.matrix[j][i] == self.players[1]:
                    sum_mark_player_two += 1
            if sum_mark_player_one == 3:
                return self.players[0]
            if sum_mark_player_two == 3:
                return self.players[1]
        #check digonal 1
        sum_mark_player_one = 0
        sum_mark_player_two = 0
        j= 0
        for i in range(3):
            if self.matrix[i][j] == self.players[0]:
                sum_mark_player_one += 1
            if self.matrix[i][j] == self.players[1]:
                sum_mark_player_two += 1
            if sum_mark_player_one == 3:
                return self.players[0]
            if sum_mark_player_two == 3:
                return self.players[1]
            j += 1

        #check digonal 2
        sum_mark_player_one = 0
        sum_mark_player_two = 0
        j= 2
        for i in range(3):
            if self.matrix[i][j] == self.players[0]:
                sum_mark_player_one += 1
            if self.matrix[i][j] == self.players[1]:
                sum_mark_player_two += 1
            if sum_mark_player_one == 3:
                return self.players[0]
            if sum_mark_player_two == 3:
                return self.players[1]
            j -= 1

        if self.round_game == 9:
            return 'Draw'
        #no player
        return None
