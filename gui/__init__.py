from .constants import *
from bresenham import Bresenham
import pygame

class Window:
    def __init__(self, width = WIDTH, height = HEIGHT):   
        pygame.init()
        pygame.font.init()

        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)
        self.bresenham = Bresenham()

        self.font = pygame.font.SysFont("Consolas", 15)

        self.start_pair = None
        self.end_pair = None

        self.line_on_screen = []

        pygame.mouse.set_visible(False)

    def draw_point(self, x, y):
        self.win.set_at((x, y), LINE_COLOR)

    def draw_line(self, x1, y1, x2, y2):
        self.bresenham.line(x1, y1, x2, y2)
        pygame.draw.circle(self.win, BLACK, (x1, y1), RADIUS_POINT // 2)
        pygame.draw.circle(self.win, BLACK, (x2, y2), RADIUS_POINT // 2)

        start_point_mess = self.font.render(f"({x1},{y1})", True, BLACK, WHITE)
        end_point_mess = self.font.render(f"({x2},{y2})", True, BLACK, WHITE)
        self.win.blit(start_point_mess, (x1 - start_point_mess.get_width() // 2 ,y1 - start_point_mess.get_height() - RADIUS_POINT))
        self.win.blit(end_point_mess, (x2 - end_point_mess.get_width() // 2, y2 - end_point_mess.get_height() - RADIUS_POINT))

        for point in self.bresenham.points:
            self.draw_point(point[0], point[1])

    def draw_all_lines(self):
        for line in self.line_on_screen:
            self.draw_line(*line)

    def draw_cursor_point(self, mouse_pos):
        if not self.start_pair:
            pygame.draw.circle(self.win, START_POINT_COLOR, mouse_pos, RADIUS_POINT) 
        elif not self.end_pair:
            pygame.draw.circle(self.win, END_POINT_COLOR, mouse_pos, RADIUS_POINT) 

    def draw_start_point(self):
        if self.start_pair:
            pygame.draw.circle(self.win, START_POINT_COLOR, self.start_pair, RADIUS_POINT) 

    def draw(self, mouse_pos):
        self.win.fill(BG_COLOR)
        self.draw_all_lines()
        self.draw_start_point()
        self.draw_cursor_point(mouse_pos)
        pygame.display.update()

    def chose_points(self, event, mouse_pos):
        x, y = mouse_pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.start_pair = (x, y)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.end_pair = (x, y)

        if self.start_pair and self.end_pair:
            self.line_on_screen.append((self.start_pair[0], self.start_pair[1], self.end_pair[0], self.end_pair[1]))
            self.start_pair = None
            self.end_pair = None

    def erase_lines(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.line_on_screen = []

    def loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            mouse_pos = pygame.mouse.get_pos()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.chose_points(event, mouse_pos)
                self.erase_lines(event)
            self.draw(mouse_pos)

        pygame.quit()