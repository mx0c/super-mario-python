import pygame
import sys

from classes.Spritesheet import Spritesheet
from classes.GaussianBlur import GaussianBlur
# Pause background will use a blurred snapshot of the last displayed screen

class Pause:
    def __init__(self, screen, entity, dashboard):
        self.screen = screen
        self.entity = entity
        self.dashboard = dashboard
        self.state = 0
        self.spritesheet = Spritesheet("./img/title_screen.png")
        # Use same banner and dots as main Menu to keep consistent style
        self.menu_banner = self.spritesheet.image_at(
            0,
            60,
            2,
            colorkey=[255, 0, 220],
            ignoreTileSize=True,
            xTileSize=180,
            yTileSize=88,
        )
        self.pause_srfc = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.pause_srfc.fill((0, 0, 0, 160))
        self.dot = self.spritesheet.image_at(
            0, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )
        self.gray_dot = self.spritesheet.image_at(
            20, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )

    def drawMenuBackground(self):
        # draw a background like the main menu using the current level's sprites
        try:
            level = self.entity.levelObj
            for y in range(0, 13):
                for x in range(0, 20):
                    self.screen.blit(
                        level.sprites.spriteCollection.get("sky").image,
                        (x * 32, y * 32),
                    )
            for y in range(13, 15):
                for x in range(0, 20):
                    self.screen.blit(
                        level.sprites.spriteCollection.get("ground").image,
                        (x * 32, y * 32),
                    )
            self.screen.blit(self.menu_banner, (150, 80))
            # small decorative sprites
            self.screen.blit(
                level.sprites.spriteCollection.get("mario_idle").image,
                (2 * 32, 12 * 32),
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_1").image, (14 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (15 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (16 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (17 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_3").image, (18 * 32, 12 * 32)
            )
            self.screen.blit(level.sprites.spriteCollection.get("goomba-1").image, (18.5*32, 12*32))
        except Exception:
            # fallback: dim overlay
            self.screen.blit(self.pause_srfc, (0, 0))

    def update(self):
        # blit blurred snapshot captured at pause time (fallback uses current overlay)
        if self.pause_srfc is None:
            self.createBackgroundBlur()
        self.screen.blit(self.pause_srfc, (0, 0))
        # subtle darkening to keep text readable
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 80))
        self.screen.blit(overlay, (0, 0))
        self.dashboard.drawText("PAUSED", 120, 160, 68)
        self.dashboard.drawText("CONTINUE", 180, 280, 24)
        self.dashboard.drawText("BACK", 180, 320, 24)
        self.drawDot()
        pygame.display.update()
        self.checkInput()

    def drawDot(self):
        ys = [280, 320]
        for i, y in enumerate(ys):
            if self.state == i:
                self.screen.blit(self.dot, (145, y))
            else:
                self.screen.blit(self.gray_dot, (145, y))

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.state == 0:
                        self.entity.pause = False
                    elif self.state == 1:
                        self.entity.restart = True
                elif event.key == pygame.K_UP:
                    if self.state > 0:
                        self.state -= 1
                elif event.key == pygame.K_DOWN:
                    if self.state < 1:
                        self.state += 1

    def createBackgroundBlur(self):
        # capture last frame and apply Gaussian blur; fallback to translucent overlay on error
        w, h = self.screen.get_size()
        try:
            self.pause_srfc = GaussianBlur().filter(self.screen, 0, 0, w, h)
            dark = pygame.Surface((w, h), pygame.SRCALPHA)
            dark.fill((0, 0, 0, 60))
            self.pause_srfc.blit(dark, (0, 0))
        except Exception:
            self.pause_srfc = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            self.pause_srfc.fill((0, 0, 0, 160))


class EditorPause:
    """Pause menu used in the Level Editor (CONTINUE, SAVE, BACK TO MENU)"""
    def __init__(self, screen, editor, dashboard):
        self.screen = screen
        self.editor = editor
        self.dashboard = dashboard
        self.state = 0
        self.spritesheet = Spritesheet("./img/title_screen.png")
        # Use same banner and dots as main Menu to keep consistent style
        self.menu_banner = self.spritesheet.image_at(
            0,
            60,
            2,
            colorkey=[255, 0, 220],
            ignoreTileSize=True,
            xTileSize=180,
            yTileSize=88,
        )
        # translucent overlay kept as fallback
        self.pause_srfc = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.pause_srfc.fill((0, 0, 0, 160))
        self.dot = self.spritesheet.image_at(
            0, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )
        self.gray_dot = self.spritesheet.image_at(
            20, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )

    def drawMenuBackground(self):
        # draw a background like the main menu using the editor's level sprites
        try:
            level = self.editor.level
            for y in range(0, 13):
                for x in range(0, 20):
                    self.screen.blit(
                        level.sprites.spriteCollection.get("sky").image,
                        (x * 32, y * 32),
                    )
            for y in range(13, 15):
                for x in range(0, 20):
                    self.screen.blit(
                        level.sprites.spriteCollection.get("ground").image,
                        (x * 32, y * 32),
                    )
            #self.screen.blit(self.menu_banner, (150, 80))
            # decorative sprites
            self.screen.blit(
                level.sprites.spriteCollection.get("mario_idle").image,
                (2 * 32, 12 * 32),
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_1").image, (14 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (15 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (16 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_2").image, (17 * 32, 12 * 32)
            )
            self.screen.blit(
                level.sprites.spriteCollection.get("bush_3").image, (18 * 32, 12 * 32)
            )
            self.screen.blit(level.sprites.spriteCollection.get("goomba-1").image, (18.5*32, 12*32))
        except Exception:
            self.screen.blit(self.pause_srfc, (0, 0))

    def update(self):
        # Use blurred snapshot captured at pause as background (captured by caller)
        if not hasattr(self, 'pause_srfc') or self.pause_srfc is None:
            self.createBackgroundBlur()
        self.screen.blit(self.pause_srfc, (0, 0))
        # subtle dark overlay for readability
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 80))
        self.screen.blit(overlay, (0, 0))
        self.dashboard.drawText("PAUSED", 120, 160, 68)
        self.dashboard.drawText("CONTINUE", 180, 280, 24)
        self.dashboard.drawText("SAVE", 180, 320, 24)
        self.dashboard.drawText("BACK TO MENU", 180, 360, 24)
        self.drawDot()
        pygame.display.update()
        self.checkInput()

    def drawDot(self):
        ys = [280, 320, 360]
        for i, y in enumerate(ys):
            if self.state == i:
                self.screen.blit(self.dot, (145, y))
            else:
                self.screen.blit(self.gray_dot, (145, y))

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.state == 0:
                        # Continue
                        self.editor.paused = False
                    elif self.state == 1:
                        # Save
                        self.editor.save_level()
                        # small confirmation
                        self.editor.input_text = "SAVED!"
                    elif self.state == 2:
                        # Back to main menu
                        self.editor.exit_to_menu = True
                elif event.key == pygame.K_UP:
                    if self.state > 0:
                        self.state -= 1
                elif event.key == pygame.K_DOWN:
                    if self.state < 2:
                        self.state += 1

    def createBackgroundBlur(self):
        # capture last frame and apply Gaussian blur; fallback to translucent overlay on error
        w, h = self.screen.get_size()
        try:
            self.pause_srfc = GaussianBlur().filter(self.screen, 0, 0, w, h)
            dark = pygame.Surface((w, h), pygame.SRCALPHA)
            dark.fill((0, 0, 0, 60))
            self.pause_srfc.blit(dark, (0, 0))
        except Exception:
            self.pause_srfc = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            self.pause_srfc.fill((0, 0, 0, 160))
