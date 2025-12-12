import pygame

from classes.Animation import Animation
from classes.Camera import Camera
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Input import Input
from classes.Sprites import Sprites
from entities.EntityBase import EntityBase
from entities.Mushroom import RedMushroom
from traits.bounce import bounceTrait
from traits.go import GoTrait
from traits.jump import JumpTrait
from classes.Pause import Pause

# -------------------------------------------------
#  ANIMASI GLOBAL
# -------------------------------------------------
spriteCollection = Sprites().spriteCollection

smallAnimation = Animation(
    [
        spriteCollection["mario_run1"].image,
        spriteCollection["mario_run2"].image,
        spriteCollection["mario_run3"].image,
    ],
    spriteCollection["mario_idle"].image,
    spriteCollection["mario_jump"].image,
)

bigAnimation = Animation(
    [
        spriteCollection["mario_big_run1"].image,
        spriteCollection["mario_big_run2"].image,
        spriteCollection["mario_big_run3"].image,
    ],
    spriteCollection["mario_big_idle"].image,
    spriteCollection["mario_big_jump"].image,
)

putihAnimation = Animation(
    [
        spriteCollection["mario_putih_run1"].image,
        spriteCollection["mario_putih_run2"].image,
        spriteCollection["mario_putih_run3"].image,
    ],
    spriteCollection["mario_putih_idle"].image,
    spriteCollection["mario_putih_jump"].image,
)


# ============================================================
#   M A R I O    C L A S S
# ============================================================

class Mario(EntityBase):

    def __init__(self, x, y, level, screen, dashboard, sound, gravity=0.8):
        super(Mario, self).__init__(x, y, gravity)

        # Spawn checkpoint
        self.spawn_x = x
        self.spawn_y = y

        self.lives = 3
        self.powerup = None
        self.dead = False

        self.camera = Camera(self.rect, self)
        self.sound = sound
        self.input = Input(self)

        self.inAir = False
        self.inJump = False
        self.powerUpState = 0
        self.invincibilityFrames = 0

        # Traits
        self.traits = {
            "jumpTrait": JumpTrait(self),
            "goTrait": GoTrait(smallAnimation, screen, self.camera, self),
            "bounceTrait": bounceTrait(self),
        }

        self.levelObj = level
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)

        self.screen = screen
        self.dashboard = dashboard
        self.restart = False

        self.pause = False
        self.pauseObj = Pause(screen, self, dashboard)

    # ----------------------------------------------------------
    # UPDATE
    # ----------------------------------------------------------
    def update(self):
        if self.invincibilityFrames > 0:
            self.invincibilityFrames -= 1

        self.updateTraits()
        self.moveMario()
        self.camera.move()
        self.applyGravity()
        self.checkEntityCollision()
        self.input.checkForInput()

        # Save checkpoint
        self.spawn_x = self.rect.x
        self.spawn_y = self.rect.y

    # ----------------------------------------------------------
    # MOVEMENT
    # ----------------------------------------------------------
    def moveMario(self):
        self.rect.y += self.vel.y
        self.collision.checkY()

        self.rect.x += self.vel.x
        self.collision.checkX()

    # ----------------------------------------------------------
    # ENTITY COLLISION
    # ----------------------------------------------------------
    def checkEntityCollision(self):
        for ent in self.levelObj.entityList[:]:
            state = self.EntityCollider.check(ent)

            if not state.isColliding:
                continue

            if ent.type.lower() == "item":
                self._onCollisionWithItem(ent)

            elif ent.type == "Block":
                self._onCollisionWithBlock(ent)

            elif ent.type == "Mob":
                self._onCollisionWithMob(ent, state)

    # ----------------------------------------------------------
    # ITEM COLLISION
    # ----------------------------------------------------------
    def _onCollisionWithItem(self, item):

        # Hindari item diambil 2x
        if hasattr(item, "taken") and item.taken:
            return
        item.taken = True

        item.alive = False

        # mainkan suara (jika ada)
        try:
            item.sound.itemSound.play()
        except:
            pass

        cls = item.__class__.__name__

        # FIRE FLOWER → Mario Putih
        if cls == "FireFlower":
            self.get_powerup("fireflower")
            return

        # RED MUSHROOM
        if cls == "RedMushroom":
            self.get_powerup("mushroom")
            return

        # COIN
        if cls == "Coin":
            self.dashboard.points += 100
            self.dashboard.coins += 1
            self.sound.play_sfx(self.sound.coin)
            return

    # ----------------------------------------------------------
    # BLOCK COLLISION
    # ----------------------------------------------------------
    def _onCollisionWithBlock(self, block):
        if not block.triggered:
            self.dashboard.coins += 1
            self.sound.play_sfx(self.sound.bump)
        block.triggered = True

    # ----------------------------------------------------------
    # MOB COLLISION
    # ----------------------------------------------------------
    def _onCollisionWithMob(self, mob, state):
        if isinstance(mob, RedMushroom) and mob.alive:
            self.get_powerup("mushroom")
            self.killEntity(mob)
            self.sound.play_sfx(self.sound.powerup)

        elif state.isTop and (mob.alive or mob.bouncing):
            self.sound.play_sfx(self.sound.stomp)
            self.rect.bottom = mob.rect.top
            self.bounce()
            self.killEntity(mob)

        elif state.isColliding and mob.alive and not self.invincibilityFrames:
            if self.powerUpState == 0:
                self.die()
            else:
                self.powerUpState = 0
                self.traits['goTrait'].updateAnimation(smallAnimation)

                bottom = self.rect.bottom
                self.rect = pygame.Rect(self.rect.x, bottom - 32, 32, 32)

                self.invincibilityFrames = 60
                self.sound.play_sfx(self.sound.pipe)

    # ----------------------------------------------------------
    def bounce(self):
        self.traits["bounceTrait"].jump = True

    def killEntity(self, ent):
        ent.alive = False
        self.dashboard.points += 100

    # ----------------------------------------------------------
    # POWER UP SYSTEM
    # ----------------------------------------------------------
    def get_powerup(self, powerup_type):
        powerup_type = powerup_type.lower()
        bottom = self.rect.bottom

        # Jamur → Mario Besar
        if powerup_type == "mushroom":
            self.powerup = "mushroom"
            self.traits['goTrait'].updateAnimation(bigAnimation)
            self.powerUpState = 1

            self.rect = pygame.Rect(self.rect.x, bottom - 64, 32, 64)
            self.invincibilityFrames = 20
            self.sound.play_sfx(self.sound.powerup)

        # Fire Flower → Mario Putih
        elif powerup_type in ("fireflower", "fire"):
            self.powerup = "fireflower"
            self.traits['goTrait'].updateAnimation(putihAnimation)
            self.powerUpState = 1

            self.rect = pygame.Rect(self.rect.x, bottom - 64, 32, 64)
            self.invincibilityFrames = 20
            self.sound.play_sfx(self.sound.powerup)

    # ----------------------------------------------------------
    # LIFE & DEATH
    # ----------------------------------------------------------
    def die(self):
        if not self.dead:
            self.dead = True
            self.lives -= 1
            self.sound.play_sfx(self.sound.stomp)

            if self.lives <= 0:
                self.gameOver()
            else:
                self.invincibilityFrames = 60
                self.respawn()

    # ----------------------------------------------------------
    def respawn(self):
        self.rect.x = self.spawn_x - 250
        self.rect.y = self.spawn_y - 500

        self.vel.x = 0
        self.vel.y = 0

        self.camera.x = max(self.spawn_x - 200, 0)
        self.camera.target_rect = self.rect

        self.dead = False

    # ----------------------------------------------------------
    # POSITION UTILITY
    # ----------------------------------------------------------
    def getPos(self):
        return self.camera.x + self.rect.x, self.rect.y

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y
