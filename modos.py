import pygame
import sys
from scene_one import ModeEasy
from scene_two import ModeIntermediate
from scene_three import ModeDifficult

ancho = 800
alto = 600
windows = pygame.display.set_mode((ancho, alto))

fondo = pygame.image.load("assets/image/home.jpg")
fondo_rect = fondo.get_rect()
pos_x = (ancho - fondo_rect.width) // 2
pos_y = (alto - fondo_rect.height) // 2

# Escalar iconos de música
icon_music_on = pygame.image.load("assets/image/sonido.png")
icon_music_off = pygame.image.load("assets/image/sin-sonido.png")
icon_music_on = pygame.transform.scale(icon_music_on, (20,20))
icon_music_off = pygame.transform.scale(icon_music_off, (20,20))

clock = pygame.time.Clock()

frames = [
    pygame.image.load("assets/image/run1.png"),
    pygame.image.load("assets/image/run2.png"),
    pygame.image.load("assets/image/run3.png")
]

frames = [pygame.transform.scale(img, (80,80)) for img in frames ]

class ModoPlayer:
    def __init__(self):
        #Fuente, Contenido y centrar boton
        self.fuente  = pygame.font.Font("fonts/light_pixel-7.ttf", 30)
        self.txt = self.fuente.render("Seleccione modo de juego", True, (255,255,255))
        self.txt_rect = self.txt.get_rect(center=(ancho // 2, 100))
        #colores de boton de sonido
        self.color_bs = (153,88,42)
        self.color_hover = (200,120,60)
        # Botón de música arriba izquierda
        self.btn_music = pygame.Rect(10, 10, 50, 50)
        self.sonido = True
        #Crear Botones, eje x - y y ancho - alto
        self.btn1 = pygame.Rect(250, 160, 300, 60)
        self.btn2 = pygame.Rect(250, 240, 300, 60)
        self.btn3 = pygame.Rect(250, 320, 300, 60)
        self.font_btn = pygame.font.Font("fonts/FlappyBirdy.ttf", 40)

        self.x = 0
        self.y = alto - 100
        self.velocidad = 5
        self.frame = 0
        self.personaje_surf = pygame.Surface((80,80), pygame.SRCALPHA)

    def ejecutarSeccion(self):
        try: 
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.btn_music.collidepoint(event.pos):
                            if self.sonido:
                                pygame.mixer.music.pause()
                                self.sonido = False
                            else:
                                pygame.mixer.music.unpause()
                                self.sonido = True
                        if self.btn1.collidepoint(event.pos):
                            modoEasy = ModeEasy()
                            modoEasy.ejecutarModeEasy()
                        if self.btn2.collidepoint(event.pos):
                            modeIntermediate = ModeIntermediate()
                            modeIntermediate.ejecutarModeIntermediate()
                        if self.btn3.collidepoint(event.pos):
                            modeDifficult = ModeDifficult()
                            modeDifficult.ejecutarModeDifficult()
                    if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
                        return
                
                windows.fill((30,30,30))
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
                windows.blit(self.txt, self.txt_rect)

                # Elegir icono
                icono_actual = icon_music_on if self.sonido else icon_music_off
                icon_rect = icono_actual.get_rect(center=btn_music_actual.center)
                windows.blit(icono_actual, icon_rect)

                #btn 1
                pygame.draw.rect(windows, (153,88,42), self.btn1, border_radius=10)
                txt1 = self.font_btn.render("Modo Facil", True, (255,255,255))
                windows.blit(txt1, txt1.get_rect(center=self.btn1.center))
                #btn 2
                pygame.draw.rect(windows, (153,88,42), self.btn2, border_radius=10)
                txt2 = self.font_btn.render("Modo Intermedio", True, (255,255,255))
                windows.blit(txt2, txt2.get_rect(center=self.btn2.center))
                #btn 3
                pygame.draw.rect(windows, (153,88,42), self.btn3, border_radius=10)
                txt3 = self.font_btn.render("Modo Dificl", True, (255,255,255))
                windows.blit(txt3, txt3.get_rect(center=self.btn3.center))

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


            
            

