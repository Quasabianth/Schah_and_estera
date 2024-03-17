import Point
import Figure


def start_game():
    with open('input.txt') as input_file:
        inp = input_file.readline().rstrip()
        while inp:
            name, color, pos = map(str, inp.split())
            pos_x, pos_y = int(pos[0]), int(pos[1])
            assert 1 <= pos_x <= 8
            assert 1 <= pos_y <= 8
            if name == "pawn":
                points[pos_x][pos_y].object = Figure.Pawn(color, points[pos_x][pos_y])
            elif name == "rook":
                points[pos_x][pos_y].object = Figure.Rook(color, points[pos_x][pos_y])
            elif name == "bishop":
                points[pos_x][pos_y].object = Figure.Bishop(color, points[pos_x][pos_y])
            elif name == "knight":
                points[pos_x][pos_y].object = Figure.Knight(color, points[pos_x][pos_y])
            elif name == "king":
                points[pos_x][pos_y].object = Figure.King(color, points[pos_x][pos_y])
            elif name == "queen":
                points[pos_x][pos_y].object = Figure.Queen(color, points[pos_x][pos_y])
            else:
                raise TypeError
            inp = input_file.readline().rstrip()


if __name__ == '__main__':
    points = [[Point.Point(x, y, None) for x in range(1, 9)] for y in range(1, 9)]
    start_game()
