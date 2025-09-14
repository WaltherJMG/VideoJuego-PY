import pygame
import sys

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))

fondo = pygame.image.load("modos.jpg")
fondo_rect = fondo.get_rect()
pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

class ModoPlayer:
    def __init__(self):
        #Fuente, Contenido y centrar boton
        self.fuente  = pygame.font.Font(None, 50)
        self.txt = self.fuente.render("Seleccione modo de juego", True, (255,255,255))
        self.txt_rect = self.txt.get_rect(center=(ancho // 2, 100))
        #Crear Botones, eje x - y y ancho - lato
        self.btn1 = pygame.Rect(250, 200,300,60)
        self.btn2 = pygame.Rect(250, 300, 300, 60)
        self.font_btn = pygame.font.Font(None, 40)

    def ejecutarSeccion(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn1.collidepoint(event.pos):
                        print("Modo de Juego 1 Seleccionado")
                    if self.btn2.collidepoint(event.pos):
                        print("Modo de Juego 2 Seleccionado")
                if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
                    return
            
            windows.fill((30,30,30))
            windows.blit(fondo, (pos_x, pos_y))
            
            windows.blit(self.txt, self.txt_rect)

            pygame.draw.rect(windows, (0,100,255), self.btn1, border_radius=10)
            txt1 = self.font_btn.render("Modo Facil", True, (255,255,255))
            windows.blit(txt1, txt1.get_rect(center=self.btn1.center))
            
            pygame.draw.rect(windows, (0,100,255), self.btn2, border_radius=10)
            txt2 = self.font_btn.render("Modo Intermedio", True, (255,255,255))
            windows.blit(txt2, txt2.get_rect(center=self.btn2.center))

            pygame.display.flip()
            
            

