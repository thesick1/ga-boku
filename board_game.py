class GameBoard:
    def __init__(self):
        self.size =  15
        self.game_board = self.__create_board()

    def __create_board(self):

        board = []
        new_row = []
        row_elements = 5
        flag = True         # flag pra saber se ele ta antes ou depois da metade do tabuleiro

        while row_elements >= 5:
        
          for i in range(0, row_elements):
              new_row.append(0)

          if row_elements < self.size and flag:
              row_elements += 1
          else:
              row_elements -= 1
              flag = False

          board.append(new_row)
          new_row = []

        return board

    def remove_piece_at(self, x: int, y: int):
        self.game_board[y][x] = 0

    def __str__(self):
        board = ""

        for row in self.game_board:
            word = ""
            for pos in row:
                word += "{0} ".format(pos)
            word = word.center(self.size*2)    
            word += "\n"
            board += word    
            
        return board

    # coloca a peca de um determinado jogador no tabuleiro
    def player_move(self, player, x, y):
        self.game_board[y][x] = player
    
    # verifica se o jogador ganhou
    def win(self):
        flag = 1
        for i in range(0,len(self.game_board)-1):
            for j in range(0,len(self.game_board[i])):
                if not self.game_board[i][j] == 0:
                    if self.win_horizontal(self.game_board,i,j,flag) or self.win_left_diagonal(self.game_board,i,j,flag) or self.win_right_diagonal(self.game_board,i,j,flag):
                        return True

        return False

    # verifica se o jogador ganhou na horizontal
    def win_horizontal(self, board, x, y, flag):
        player = board[x][y]
        row_size = len(board[x])-1
        if row_size >= y+1:
            if board[x][y+1] == player:
                flag += 1
                if flag == 5:
                    return True
                else:
                    return self.win_horizontal(board,x,y+1,flag)

        return False

    def win_left_diagonal(self, board, x, y, flag):
        player = board[x][y]
        middle_row = (len(board)-1)/2  # pega o indice da linha do meio
        board_size = len(board)-1 # isso retorna quantas colunas aquela linha tem
        if board_size >= x+1:
            row_size = len(board[x+1])-1
            if row_size >= y:
                if x < middle_row:
                    if board[x+1][y] == player:
                        flag += 1
                        if flag == 5:
                            return True
                        else:
                            return self.win_left_diagonal(board,x+1,y,flag)
                else:
                    if board[x+1][y-1] == player:
                        flag += 1
                        if flag == 5:
                            return True
                        else:
                            return self.win_left_diagonal(board,x+1,y-1,flag)
        
        return False

    def win_right_diagonal(self, board, x, y, flag):
        player = board[x][y]
        middle_row = (len(board)-1)/2  # pega o indice da linha do meio
        board_size = len(board)-1
        if board_size >= x+1:
            row_size = len(board[x+1])-1
            if x < middle_row:    
                if row_size >= y+1:
                    if board[x+1][y+1] == player:
                        flag += 1
                        if flag == 5:
                            return True
                        else:
                            return self.win_right_diagonal(board,x+1,y+1,flag)
            else:
                if row_size >= y:
                    if board[x+1][y] == player:
                        flag += 1
                        if flag == 5:
                            return True
                        else:
                            return self.win_right_diagonal(board,x+1,y,flag)
        
        return False