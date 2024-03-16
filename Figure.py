class Figure:
    pass

class Pawn(Figure):
    def __init__(self, pos: str, color: int):
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.color = color
        self.moves = self.move()

    def move(self) -> set:
        moves = []
        assert self.pos_y != 8
        assert self.pos_y != 1
        if self.color == 0:
            cand = [str(self.pos_x + a) + str(self.pos_y + 1) for a in [-1, 0, 1]]
            for tr in cand:
                if 1 <= int(tr[0]) <= 8:
                    moves.append(tr)
            if self.pos_y == 2:
                moves.append(str(self.pos_x + 1) + str(4))
        elif self.color == 1:
            cand = [str(self.pos_x + a) + str(self.pos_y - 1) for a in [-1, 0, 1]]
            for tr in cand:
                if 1 <= int(tr[0]) <= 8:
                    moves.append(tr)
            if self.pos_y == 7:
                moves.append(str(self.pos_x + 1) + str(5))
        return set(moves)

    def delete(self):
        pass
