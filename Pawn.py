import pygame
import math

WIDTH, HEIGHT = 800,800
# win = pygame.display.set_mode((WIDTH,HEIGHT))


class Pawn:
    def __init__(self, number, center_x, center_y, size, player):
        self.number = number
        self.center_x = center_x
        self.center_y = center_y
        self.pressed = False
        self.color = 'white'
        self.player = player
        self.vertices = []
        self.size = size
        # Calculating tops of hex
        for i in range(1,7):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            self.vertices.append((self.center_x + self.size * math.cos(angle_rad),
                                  self.center_y + self.size * math.sin(angle_rad)))
    # Drawin hex
    # def draw_pawn(self):
    #     pygame.draw.polygon(win, self.color,[self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3],self.vertices[4],self.vertices[5]])
    #     # Rysowanie konturów
    #     pygame.draw.line(win,'black',self.vertices[1],self.vertices[2])
    #     pygame.draw.line(win,'black',self.vertices[2],self.vertices[3])
    #     pygame.draw.line(win,'black',self.vertices[3],self.vertices[4])

    def click_pawn(self, mouse_pos):
        if (mouse_pos[0] > self.vertices[1][0]-5 and mouse_pos[0] < self.vertices[0][0]+5):
            if (mouse_pos[1] > self.vertices[3][1] and mouse_pos[1] < self.vertices[1][1]):
                return True
                

    
    def move_tile_set(self, number, player):
        if self.number == number:
            if player == 1:
                self.color = 'green'
                self.player = 1
            else:
                self.color = 'red'
                self.player = 2