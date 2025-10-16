class Bresenham:
    def __init__(self):
        self.points = []
        
    def line(self, x1, y1, x2, y2):
        self.points = []
        
        delta_x = abs(x2 - x1)
        delta_y = abs(y2 - y1)
        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1
        x = x1
        y = y1

        if delta_y < delta_x: # |slope| < 1
            p = 2 * delta_y - delta_x
            for _ in range(delta_x + 1):
                self.points.append((x, y))
                x += step_x
                if p >= 0:
                    y += step_y
                    p += 2 *delta_y - 2*delta_x
                else:
                    p += 2 * delta_y

        else: # |slope| >= 1
            p = 2 * delta_x - delta_y
            for _ in range(delta_y + 1):
                self.points.append((x, y))
                y += step_y
                if p >= 0:
                    x += step_x
                    p += 2 * delta_x - 2 * delta_y
                else:
                    p += 2 * delta_x