import Point


class Figure:
    pass


class Pawn(Figure):
    def __init__(self, color: int, point: Point):
        self.color = color
        self.moves = self.move()
        self.point = point

    def move(self) -> set:
        moves = []
        assert self.point.pos_y != 1
        assert self.point.pos_y != 8
        if self.color == 0:
            cand = [str(self.point.pos_x + a) + str(self.point.pos_y + 1) for a in [-1, 0, 1]]
            for tr in cand:
                if 1 <= int(tr[0]) <= 8:
                    moves.append(tr)
            if self.point.pos_y == 2:
                moves.append(str(self.point.pos_x + 1) + str(4))
        elif self.color == 1:
            cand = [str(self.point.pos_x + a) + str(self.point.pos_y - 1) for a in [-1, 0, 1]]
            for tr in cand:
                if 1 <= int(tr[0]) <= 8:
                    moves.append(tr)
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

    def move(self) -> set:
        moves = [str(self.point.pos_x + a) + str(self.point.pos_y + b) for a in [-1, 0, 1] for b in [-1, 0, 1]
                 if 1 <= self.point.pos_x + a <= 8
                 if 1 <= self.point.pos_y + b <= 8]
        return set(moves)

    def delete(self):
        pass
