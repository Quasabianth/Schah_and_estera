import Point


class Figure:
    def __init__(self, color: str, point: Point):
        self.color = color
        self.point = point

    def delete(self):
        self.point.object = None
        self.point = None

    def move_figure(self, point: Point):
        if point.object:
            point.object.point = None
        self.point.object = None
        point.object = self
        self.point = point


class Pawn(Figure):
    def __init__(self, color: str, point: Point):
        Figure.__init__(self, color, point)
        self.moves = self.move()
        self.identifier = 'Pawn'

    def move(self) -> set:
        moves = []
        assert self.point.pos_y != 1
        assert self.point.pos_y != 8
        if self.color == 'w':
            moves += [str(self.point.pos_x + a) + str(self.point.pos_y + 1) for a in [-1, 0, 1]
                      if 1 <= self.point.pos_x + a <= 8]
            if self.point.pos_y == 2:
                moves.append(str(self.point.pos_x + 1) + str(4))
        elif self.color == 'b':
            moves = [str(self.point.pos_x + a) + str(self.point.pos_y - 1) for a in [-1, 0, 1]
                     if 1 <= self.point.pos_x + a <= 8]
            if self.point.pos_y == 7:
                moves.append(str(self.point.pos_x + 1) + str(5))
        return set(moves)

    def possible_moves(self, points: list[list[Point.Point]]) -> set:
        moves = set()
        if self.color == 'w':
            if points[self.point.pos_x][self.point.pos_y + 1].object is None:
                moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                          str(self.point.pos_x) + str(self.point.pos_y + 1))
                if self.point.pos_y == 2:
                    if points[self.point.pos_x][self.point.pos_y + 2].object is None:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x) + str(self.point.pos_y + 2))
            if 1 <= self.point.pos_x <= 7:
                if points[self.point.pos_x + 1][self.point.pos_y + 1].object is not None:
                    if points[self.point.pos_x - 1][self.point.pos_y + 1].object.color != self.color:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x + 1) + str(self.point.pos_y + 1))
            if 2 <= self.point.pos_x <= 8:
                if points[self.point.pos_x - 1][self.point.pos_y + 1].object is not None:
                    if points[self.point.pos_x - 1][self.point.pos_y + 1].object.color != self.color:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x - 1) + str(self.point.pos_y + 1))
        elif self.color == 'b':
            if points[self.point.pos_x][self.point.pos_y - 1].object is None:
                moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                          str(self.point.pos_x) + str(self.point.pos_y - 1))
                if self.point.pos_y == 7:
                    if points[self.point.pos_x][self.point.pos_y - 2].object is None:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x) + str(self.point.pos_y - 2))
            if 1 <= self.point.pos_x <= 7:
                if points[self.point.pos_x + 1][self.point.pos_y - 1].object is not None:
                    if points[self.point.pos_x - 1][self.point.pos_y + 1].object.color != self.color:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x + 1) + str(self.point.pos_y - 1))
            if 2 <= self.point.pos_x <= 8:
                if points[self.point.pos_x - 1][self.point.pos_y + 1].object is not None:
                    if points[self.point.pos_x - 1][self.point.pos_y + 1].object.color != self.color:
                        moves.add(str(self.point.pos_x) + str(self.point.pos_y) +
                                  str(self.point.pos_x - 1) + str(self.point.pos_y - 1))
        else:
            raise NotImplemented
        return moves


class King(Figure):
    def __init__(self, color: str, point: Point, is_castle1_possible: bool, is_castle2_possible: bool):
        Figure.__init__(self, color, point)
        self.moves = self.move()
        self.identifier = 'King'
        self.is_castle1_possible = is_castle1_possible
        self.is_castle2_possible = is_castle2_possible

    def move(self) -> set:
        moves = [str(self.point.pos_x + a) + str(self.point.pos_y + b) for a in [-1, 0, 1] for b in [-1, 0, 1]
                 if 1 <= self.point.pos_x + a <= 8
                 if 1 <= self.point.pos_y + b <= 8]
        return set(moves)

    def move_figure(self, point: Point):
        Figure.move_figure(self, point)
        self.is_castle1_possible = False
        self.is_castle2_possible = False


class Knight(Figure):
    def __init__(self, color: str, point: Point):
        Figure.__init__(self, color, point)
        self.moves = self.move()
        self.identifier = 'Knight'

    def move(self) -> set:
        moves = []
        knight_moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y + b) for a, b in knight_moves
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y + b <= 8]
        return set(moves)


class Bishop(Figure):
    def __init__(self, color: str, point: Point):
        Figure.__init__(self, color, point)
        self.moves = self.move()
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


class Rook(Figure):
    def __init__(self, color: str, point: Point, is_castle1_possible: bool, is_castle2_possible: bool):
        Figure.__init__(self, color, point)
        self.moves = self.move()
        self.is_castle2_possible = is_castle1_possible
        self.is_castle2_possible = is_castle2_possible
        self.identifier = 'Rook'

    def move(self) -> set:
        moves = []
        moves += [str(self.point.pos_x) + str(self.point.pos_y + a) for a in range(-8, 9)
                  if 1 <= self.point.pos_y + a <= 8]
        moves += [str(self.point.pos_x + b) + str(self.point.pos_y) for b in range(-8, 9)
                  if 1 <= self.point.pos_x + b <= 8]
        return set(moves)


class Queen(Figure):
    def __init__(self, color: str, point: Point):
        Figure.__init__(self, color, point)
        self.moves = self.move()
        self.identifier = 'Queen'

    def move(self) -> set:
        moves = []
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y + a) for a in range(-8, 9)
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y + a <= 8]
        moves += [str(self.point.pos_x + a) + str(self.point.pos_y - a) for a in range(-8, 9)
                  if 1 <= self.point.pos_x + a <= 8
                  if 1 <= self.point.pos_y - a <= 8]
        moves += [str(self.point.pos_x) + str(self.point.pos_y + a) for a in range(-8, 9)
                  if 1 <= self.point.pos_y + a <= 8]
        moves += [str(self.point.pos_x + b) + str(self.point.pos_y) for b in range(-8, 9)
                  if 1 <= self.point.pos_x + b <= 8]
        return set(moves)
