import pygame
import sys
from modos import ModoPlayer

pygame.init()

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()

frames = [
    pygame.image.load("image/run1.png"),
    pygame.image.load("image/run2.png"),
    pygame.image.load("image/run3.png")
]

frames = [pygame.transform.scale(img, (80,80)) for img in frames ]

pygame.display.set_caption("Juego de Trivia")

fondo = pygame.image.load("image/home.jpg")

fondo_rect = fondo.get_rect()

pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

pygame.mixer.init()
pygame.mixer.music.load("music/musica.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

class Home: 
    def __init__(self):
        self.fuente = pygame.font.Font("fonts/FlappyBirdy.ttf",300)
        self.titulo = self.fuente.render("RidDleX", True, (255,255,255))
        self.titulo_rect = self.titulo.get_rect(center=(ancho // 2, 200))

        self.btn = pygame.Rect(315, 300, 200, 60)
        self.fuente_btn = pygame.font.Font("fonts/FlappyBirdy.ttf", 50)

        self.color_bs = (153,88,42)
        self.color_hover = (200,120,60)

        self.x = 0
        self.y = alto - 100
        self.velocidad = 5
        self.frame = 0

        self.personaje_surf = pygame.Surface((80,80), pygame.SRCALPHA)
    
    def canva_btn(self, windows):
        windows.blit(self.titulo, self.titulo_rect)

        pygame.draw.rect(windows, (0,0,255), self.btn, border_radius=10)
        txt_btn = self.fuente_btn.render("Comenzar", True, (255,255,255))
        txt_btn_rect = txt_btn.get_rect(center=self.btn.center)
        windows.blit(txt_btn, txt_btn_rect)
    
    def ejecutarSeccion(self):
        global frames
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

            efect_mouse = pygame.mouse.get_pos()

            if self.btn.collidepoint(efect_mouse):
                btn_actual = pygame.Rect(self.btn.x-5,self.btn.y-5, self.btn.width+10,self.btn.height+10)
                color = self.color_hover
            else:
                btn_actual = self.btn
                color = self.color_bs
            
            sombra_btn = pygame.Rect(btn_actual.x+4, btn_actual.y+4,btn_actual.width, btn_actual.height)
            pygame.draw.rect(windows, (50,50,50), sombra_btn, border_radius=10)

            pygame.draw.rect(windows, color, btn_actual, border_radius=10)
            txt_btn = self.fuente_btn.render("Comenzar", True, (255,255,255))
            txt_btn_rect = txt_btn.get_rect(center=btn_actual.center)
            windows.blit(txt_btn, txt_btn_rect)

            self.personaje_surf.fill((0,0,0,0))
            self.personaje_surf.blit(frames[self.frame], (0,0))
            windows.blit(self.personaje_surf, (self.x, self.y))

            self.x += self.velocidad
            if self.x > ancho:
                self.x = -80
            
            
            self.frame = (self.frame + 1) % len(frames)

            pygame.display.flip()
            clock.tick(10)
