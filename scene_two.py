import pygame 
import sys

pygame.init()

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))

fondo = pygame.image.load("assets/image/home.jpg")
fondo_rect = fondo.get_rect()
pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

# icono btn Back
icon_back = pygame.image.load("assets/image/arrow-back.png")
icon_back = pygame.transform.scale(icon_back, (25, 25))  # tamaño del ícono

clock = pygame.time.Clock()

class ModeIntermediate:
    def __init__(self):
        self.tipoLetra = pygame.font.Font(None, 80)
        self.titulo = self.tipoLetra.render("Modo Intermedio", True, (255,255,255))
        self.titulo_rect = self.titulo.get_rect(center=(ancho // 2, 200))
        #btn Back
        self.btn_back = pygame.Rect(10, 10, 50, 50)  
    def ejecutarModeIntermediate(self):
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.btn_back.collidepoint(event.pos):
                            from modos import ModoPlayer
                            return ModoPlayer
                    
                windows.fill((0,0,0))
                windows.blit(fondo, (pos_x, pos_y))
                windows.blit(self.titulo, self.titulo_rect)
                # dibujar rectángulo del botón (opcional, si quieres ver el fondo del botón)
                pygame.draw.rect(windows, (153, 88, 42), self.btn_back, border_radius=8)

                # centrar el ícono dentro del botón
                icon_rect = icon_back.get_rect(center=self.btn_back.center)
                windows.blit(icon_back, icon_rect.topleft)
                pygame.display.flip()
        except Exception as e:
            print("Error: ", e)