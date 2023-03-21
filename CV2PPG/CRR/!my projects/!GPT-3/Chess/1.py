class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
            ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
            [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
            ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.current_player = 'w'
        self.game_over = False

    def print_board(self):
        for row in self.board:
            print(' '.join(str(x) for x in row))

    def get_player_input(self):
        start = input("Enter start position (e.g. 'e2'): ")
        end = input("Enter end position (e.g. 'e4'): ")
        return start, end

    def is_valid_move(self, start, end):
        # Проверяем, что стартовая и конечная позиции на доске
        if start[0] not in 'abcdefgh' or end[0] not in 'abcdefgh':
            return False
        if start[1] not in '12345678' or end[1] not in '12345678':
            return False

        # Проверяем, что начальная клетка не пуста и содержит фигуру текущего игрока
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        if self.board[start_row][start_col] == ' ' or \
                self.board[start_row][start_col].lower() != self.current_player:
            return False

        # Проверяем, что конечная клетка пуста или содержит фигуру другого игрока
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        if self.board[end_row][end_col] != ' ' and \
                self.board[end_row][end_col].lower() == self.current_player:
            return False

        # Проверяем, что фигура может двигаться из начальной клетки в конечную клетку
        if self.board[start_row][start_col].lower() == 'p':
            if start_col == end_col and self.board[end_row][end_col] == ' ':
                if start_row == 6 and end_row == 4 and self.board[5][start_col] == ' ':
                    return True
                if start_row == end_row + 1:
                    return True
            if abs(start_col - end_col) == 1 and start_row == end_row + 1 \
                    and self.board[end_row][end_col].lower() != self.current_player:
                return True
        elif self.board[start_row][start_col].lower() == 'r':
            if start_row == end_row:
                if start_col < end_col:
                    for col in start_col + 1, end_col):
                        if self.board[start_row][col] != ' ':
                            return False
                        return True
                    elif start_col > end_col:
                    for col in range(end_col + 1, start_col):
                        if self.board[start_row][col] != ' ':
                            return False
                    return True
            elif start_col == end_col:
                if start_row < end_row:
                    for row in range(start_row + 1, end_row):
                        if self.board[row][start_col] != ' ':
                            return False
                    return True
                elif start_row > end_row:
                    for row in range(end_row + 1, start_row):
                        if self.board[row][start_col] != ' ':
                            return False
                    return True
            return False
            elif self.board[start_row][start_col].lower() == 'n':
            if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
                    (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
                return True
            return False
        elif self.board[start_row][start_col].lower() == 'b':
            if abs(start_row - end_row) == abs(start_col - end_col):
                if start_row < end_row and start_col < end_col:
                    for i in range(1, end_row - start_row):
                        if self.board[start_row + i][start_col + i] != ' ':
                            return False
                    return True
                elif start_row < end_row and start_col > end_col:
                    for i in range(1, end_row - start_row):
                        if self.board[start_row + i][start_col - i] != ' ':
                            return False
                    return True
                elif start_row > end_row and start_col < end_col:
                    for i in range(1, start_row - end_row):
                        if self.board[start_row - i][start_col + i] != ' ':
                            return False
                    return True
                elif start_row > end_row and start_col > end_col:
                    for i in range(1, start_row - end_row):
                        if self.board[start_row - i][start_col - i] != ' ':
                            return False
                    return True
            return False
        elif self.board[start_row][start_col].lower() == 'q':
            if self.is_valid_move(start, end, 'r') or self.is_valid_move(start, end, 'b'):
                return True
            return False
        elif self.board[start_row][start_col].lower() == 'k':
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                return True
            return False
        return False

    def make_move(self, start, end):
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '
        self.current_player = 'b' if self.current_player == 'w' else

    def is_check(self, player):
        # Найдем позицию короля игрока
        king_pos = None
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == player + 'k':
                    king_pos = (row, col)
                    break
            if king_pos:
                break

        # Проверим угрожает ли королю противник
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ' and piece[0] != player:
                    if self.is_valid_move((row, col), king_pos):
                        return True

        return False

    def is_checkmate(self, player):
        # Проверим есть ли ходы, которыми можно уйти от шаха
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ' and piece[0] == player:
                    for row2 in range(8):
                        for col2 in range(8):
                            if self.is_valid_move((row, col), (row2, col2)):
                                temp_board = deepcopy(self.board)
                                temp_board[row2][col2] = temp_board[row][col]
                                temp_board[row][col] = ' '
                                if not self.is_check(player):
                                    return False

        return True

    def is_stalemate(self, player):
        # Проверим есть ли ходы, которыми можно сделать не шах, но и не мат
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ' and piece[0] == player:
                    for row2 in range(8):
                        for col2 in range(8):
                            if self.is_valid_move((row, col), (row2, col2)):
                                temp_board = deepcopy(self.board)
                                temp_board[row2][col2] = temp_board[row][col]
                                temp_board[row][col] = ' '
                                if not self.is_check(player):
                                    return False

        return True

    def play(self):
        while not self.is_checkmate(self.current_player) and not self.is_stalemate(self.current_player):
            print(self)
            print("Ходят", "белые" if self.current_player == 'w' else "черные")
            move = input("Введите ход в формате 'a2 a4': ")
            if not self.is_valid_move(move.split()[0], move.split()[1]):
                print("Неверный ход, попробуйте еще раз.")
                continue
            self.make_move(move.split()[0], move.split()[1])
        print(self)
        if self.is_checkmate(self.current_player):
            print("Мат. Победили", "белые" if self.current_player == 'b' else "черные")
        else:
            print("Пат. Ничья")

