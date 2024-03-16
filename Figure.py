import Point


class Figure:
    pass


class Pawn(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point
        self.identifier = 'Pawn'

    def move(self) -> set:
        moves = []
        assert self.point.pos_y != 1
        assert self.point.pos_y != 8
        if self.color == 0:
            moves += [str(self.point.pos_x + a) + str(self.point.pos_y + 1) for a in [-1, 0, 1]
                      if 1 <= self.point.pos_x + a <= 8]
            if self.point.pos_y == 2:
                moves.append(str(self.point.pos_x + 1) + str(4))
        elif self.color == 1:
            moves = [str(self.point.pos_x + a) + str(self.point.pos_y - 1) for a in [-1, 0, 1]
                     if 1 <= self.point.pos_x + a <= 8]
            if self.point.pos_y == 7:
                moves.append(str(self.point.pos_x + 1) + str(5))
        return set(moves)

    def delete(self):
        pass


class King(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point
        self.identifier = 'King'

    def move(self) -> set:
        moves = [str(self.point.pos_x + a) + str(self.point.pos_y + b) for a in [-1, 0, 1] for b in [-1, 0, 1]
                 if 1 <= self.point.pos_x + a <= 8
                 if 1 <= self.point.pos_y + b <= 8]
        return set(moves)

    def delete(self):
        pass


class Knight(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point
        self.identifier = 'Knight'

    def move(self) -> set:
        moves = []
        knight_moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y + b) for a, b in knight_moves
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y + b <= 8]
        return set(moves)

    def delete(self):
        pass


class Bishop(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point
        self.identifier = 'Bishop'

    def move(self) -> set:
        moves = []
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y + a) for a in range(-8, 9)
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y + a <= 8]
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y - a) for a in range(-8, 9)
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y - a <= 8]
        return set(moves)

    def delete(self):
        pass


class Rook(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point
        self.identifier = 'Rook'

    def move(self) -> set:
        moves = []
        moves += [str(self.point.pos_x) + str(self.point.pos_y + a) for a in range(-8, 9)
                  if 1 <= self.point.pos_y + a <= 8]
        moves += [str(self.point.pos_x + b) + str(self.point.pos_y) for b in range(-8, 9)
                  if 1 <= self.point.pos_x + b <= 8]
        return set(moves)

    def delete(self):
        pass
