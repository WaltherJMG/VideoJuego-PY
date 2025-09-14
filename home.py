import pygame
import sys
from modos import ModoPlayer

pygame.init()

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))

pygame.display.set_caption("Juego de Trivia")

fondo = pygame.image.load("home.jpg")

fondo_rect = fondo.get_rect()

pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

class Home: 
    def __init__(self):
        self.fuente = pygame.font.Font(None,100)
        self.titulo = self.fuente.render("RiddleX", True, (255,255,255))
        self.titulo_rect = self.titulo.get_rect(center=(ancho // 2, 50))

        self.btn = pygame.Rect(315, 300, 200, 60)
        self.fuente_btn = pygame.font.Font(None, 40)
    
    def canva_btn(self, windows):
        windows.blit(self.titulo, self.titulo_rect)

        pygame.draw.rect(windows, (0,0,255), self.btn, border_radius=10)
        txt_btn = self.fuente_btn.render("Comenzar", True, (255,255,255))
        txt_btn_rect = txt_btn.get_rect(center=self.btn.center)
        windows.blit(txt_btn, txt_btn_rect)
    
    def ejecutarSeccion(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn.collidepoint(event.pos):
                        modos = ModoPlayer()
                        modos.ejecutarSeccion()
            
            windows.fill((0,0,0))
            windows.blit(fondo, (pos_x, pos_y))

            windows.blit(self.titulo, self.titulo_rect)

            pygame.draw.rect(windows, (153,88,42), self.btn, border_radius=10)
            txt_btn = self.fuente_btn.render("Comenzar", True, (255,255,255))
            txt_btn_rect = txt_btn.get_rect(center=self.btn.center)
            windows.blit(txt_btn, txt_btn_rect)

            pygame.display.flip()
