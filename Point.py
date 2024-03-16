import Figure


class Point:
    def __init__(self, x: int, y: int, fig: figure):
        self.pos_x = x
        self.pos_y = y
        self.object = fig
