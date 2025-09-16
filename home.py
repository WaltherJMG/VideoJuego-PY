import pygame
import sys
from modos import ModoPlayer

pygame.init()

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()

frames = [
    pygame.image.load("assets/image/run1.png"),
    pygame.image.load("assets/image/run2.png"),
    pygame.image.load("assets/image/run3.png")
]

frames = [pygame.transform.scale(img, (80,80)) for img in frames]

pygame.display.set_caption("Juego de Trivia")

fondo = pygame.image.load("assets/image/home.jpg")
icon_music_on = pygame.image.load("assets/image/sonido.png")
icon_music_off = pygame.image.load("assets/image/sin-sonido.png")

# Escalar iconos de música
icon_music_on = pygame.transform.scale(icon_music_on, (20,20))
icon_music_off = pygame.transform.scale(icon_music_off, (20,20))

fondo_rect = fondo.get_rect()

pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

pygame.mixer.init()
pygame.mixer.music.load("music/musica.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

class Home: 
    def __init__(self):
        self.fuente = pygame.font.Font("fonts/light_pixel-7.ttf",120)
        self.titulo = self.fuente.render("RidDleX", True, (255,255,255))
        self.titulo_rect = self.titulo.get_rect(center=(ancho // 2, 200))

        # Botón de música arriba izquierda
        self.btn_music = pygame.Rect(10, 10, 50, 50)
        self.sonido = True

        # Botón comenzar
        self.btn = pygame.Rect(315, 300, 200, 60)
        self.fuente_btn = pygame.font.Font("fonts/FlappyBirdy.ttf", 50)

        self.color_bs = (153,88,42)
        self.color_hover = (200,120,60)

        self.x = 0
        self.y = alto - 100
        self.velocidad = 5
        self.frame = 0

        self.personaje_surf = pygame.Surface((80,80), pygame.SRCALPHA)

    def ejecutarSeccion(self):
        global frames
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Botón comenzar
                        if self.btn.collidepoint(event.pos):
                            modos = ModoPlayer()
                            modos.ejecutarSeccion()
                        # Botón sonido
                        if self.btn_music.collidepoint(event.pos):
                            if self.sonido:
                                pygame.mixer.music.pause()
                                self.sonido = False
                            else:
                                pygame.mixer.music.unpause()
                                self.sonido = True
                        
                        
                
                windows.fill((0,0,0))
                windows.blit(fondo, (pos_x, pos_y))

                efect_mouse = pygame.mouse.get_pos()

                # --- BOTÓN DE SONIDO ---
                if self.btn_music.collidepoint(efect_mouse):
                    btn_music_actual = pygame.Rect(self.btn_music.x, self.btn_music.y, 
                                                self.btn_music.width, self.btn_music.height)
                    color_btn_music = self.color_hover
                else:
                    btn_music_actual = self.btn_music
                    color_btn_music = self.color_bs
                
                sombra_sonido = pygame.Rect(btn_music_actual.x+4, btn_music_actual.y+4,
                                            btn_music_actual.width, btn_music_actual.height)
                pygame.draw.rect(windows, (50,50,50), sombra_sonido, border_radius=10)
                pygame.draw.rect(windows, color_btn_music, btn_music_actual, border_radius=10)

                # Elegir icono
                icono_actual = icon_music_on if self.sonido else icon_music_off
                icon_rect = icono_actual.get_rect(center=btn_music_actual.center)
                windows.blit(icono_actual, icon_rect)

                # --- TÍTULO ---
                windows.blit(self.titulo, self.titulo_rect)

                # --- BOTÓN COMENZAR ---
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

                # --- PERSONAJE ---
                self.personaje_surf.fill((0,0,0,0))
                self.personaje_surf.blit(frames[self.frame], (0,0))
                windows.blit(self.personaje_surf, (self.x, self.y))

                self.x += self.velocidad
                if self.x > ancho:
                    self.x = -80
                

                self.frame = (self.frame + 1) % len(frames)

                pygame.display.flip()
                clock.tick(10)
        except Exception as e:
            print("Error: ", e)
