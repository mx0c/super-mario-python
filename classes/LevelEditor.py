import pygame
import json
import sys, os
from classes.Tile import Tile
from classes.Pause import EditorPause

class LevelEditor:
    def __init__(self, screen, dashboard, level, sound,test_mode=False):
        self.screen = screen
        self.dashboard = dashboard
        self.level = level
        self.sound = sound

        # Clean Slate
        self.level.entityList = []
        
        # Editor State 
        self.camera_x = 0.0
        self.grid_size = 32
        self.selected_tool = 0 
        self.pipe_length = 3 

        # Scroll control: step per tick and minimum interval between steps (ms)
        self.camera_step = 1
        self.scroll_interval = 100  # milliseconds between increments when key is held
        self._last_scroll_time = 0 
        
        # Deletion State
        self.deleting = False
        self.delete_interval = 100  # ms between deletes
        self._last_delete_time = 0
        self._last_delete_cell = None


        # Level Settings
        self.level_length = 200 
        self.min_length = 60 

        # Input Box State (Top Right, Floating)
        self.input_rec = pygame.Rect(530, 10, 100, 32)
        self.input_active = False 
        self.input_text = str(self.level_length) 
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.current_color = self.color_inactive

        # The Palette
        self.tools = [
            "ground", "sky", "pipe", "bush_1", "cloud1_1",
            "Goomba", "Koopa", "coin", "CoinBox", "coinBrick"
        ]

        # Continuous placement state (hold mouse to paint)
        self.placing = False
        self.place_interval = 50  # milliseconds between automatic placements when holding
        self._last_place_time = 0
        self._last_place_cell = None
        
        self.level_data = {
            "level": {
                "objects": { "bush": [], "cloud": [], "pipe": [], "sky": [], "ground": [] },
                "entities": { "CoinBox": [], "Goomba": [], "Koopa": [], "coin": [], "coinBrick": [], "RandomBox": [] },
                "layers": {
                    "sky": {"x": [0, 200], "y": [0, 13]},
                    "ground": {"x": [0, 200], "y": [13, 15]}
                }
            },
            "length": self.level_length
        }

        # Init Sky Grid
        self.level.level = [] 
        for y in range(15):
            row = []
            for x in range(self.level_length + 100): 
                row.append(Tile(self.level.sprites.spriteCollection.get("sky"), None))
            self.level.level.append(row)
        self.level.levelLength = self.level_length

        # Start Menu State
        self.start_mode = True
        self.start_state = 0  # 0 = Create, 1 = Load
        self.pause_menu = EditorPause(self.screen, self, self.dashboard)
        self.paused = False
        self.exit_to_menu = False

        # Load Chooser (GRID)
        self.inChoosingLevel = False
        self.current_filename = None
        self.currSelectedLoad = 0
        self.load_files = []

        # test mode flag
        self.test_mode = test_mode
    
    def refresh_load_files(self):
        try:
            files = os.listdir("./levels")
        except FileNotFoundError:
            return []
        levels = [f[:-5] for f in files if f.endswith('.json')]
        levels.sort()
        return levels

    def draw_start_menu(self):
        # Use same background style as main menu/settings
        self.draw_editor_menu_background()
        if not self.inChoosingLevel:
            self.screen.blit(self.pause_menu.menu_banner, (150, 80))

        cx = self.screen.get_width() // 2

        # ===== LOAD CHOOSER MODE =====
        if self.inChoosingLevel:
            self.draw_load_chooser()
            return

        # ===== NORMAL EDITOR MENU =====
        # Smaller, cleaner title (like Settings)
        options = ["CREATE NEW LEVEL", "LOAD LEVEL", "BACK"]
        ys = [280, 320, 360]

        for i, opt in enumerate(options):
            self.dashboard.drawText(opt, cx - 140, ys[i], 24)

        # Selection dot (same style as menus)
        self.screen.blit(self.pause_menu.dot, (cx - 175, ys[self.start_state]))




    def drawBorder(self, x, y, width, height, color, thickness=5):
        pygame.draw.rect(self.screen, color, (x, y, width, thickness))
        pygame.draw.rect(self.screen, color, (x, y+height-thickness, width, thickness))
        pygame.draw.rect(self.screen, color, (x, y, thickness, height))
        pygame.draw.rect(self.screen, color, (x+width-thickness, y, thickness, height))

    def draw_load_chooser(self):
        files = self.load_files
        if not files:
            self.dashboard.drawText("NO LEVELS FOUND.", 220, 260, 18)
            return

        cols = 3
        box_w = 160
        box_h = 70
        start_x = 80
        start_y = 140
        gap_x = 200
        gap_y = 140

        for i, name in enumerate(files):
            row = i // cols
            col = i % cols

            x = start_x + col * gap_x
            y = start_y + row * gap_y

            color = (255, 255, 255) if self.currSelectedLoad == i else (150, 150, 150)

            self.drawBorder(x, y, box_w, box_h, color)
            self.dashboard.drawText(name, x + 20, y + 25, 14)

    def draw_editor_menu_background(self):
        # Mimic Menu.drawMenuBackground for consistency
        for y in range(0, 13):
            for x in range(0, 20):
                self.screen.blit(
                    self.level.sprites.spriteCollection.get("sky").image,
                    (x * 32, y * 32),
                )
        for y in range(13, 15):
            for x in range(0, 20):
                self.screen.blit(
                    self.level.sprites.spriteCollection.get("ground").image,
                    (x * 32, y * 32),
                )

        # Decorative sprites (same as Menu)
        self.screen.blit(
            self.level.sprites.spriteCollection.get("mario_idle").image,
            (2 * 32, 12 * 32),
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_1").image, (14 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (15 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (16 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_2").image, (17 * 32, 12 * 32)
        )
        self.screen.blit(
            self.level.sprites.spriteCollection.get("bush_3").image, (18 * 32, 12 * 32)
        )



    def check_start_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # ===== LOAD CHOOSER GRID MODE =====
            if self.inChoosingLevel:
                files = self.load_files
                cols = 3

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.currSelectedLoad = max(0, self.currSelectedLoad - 1)

                    elif event.key == pygame.K_RIGHT:
                        self.currSelectedLoad = min(len(files) - 1, self.currSelectedLoad + 1)

                    elif event.key == pygame.K_UP:
                        self.currSelectedLoad = max(0, self.currSelectedLoad - cols)

                    elif event.key == pygame.K_DOWN:
                        self.currSelectedLoad = min(len(files) - 1, self.currSelectedLoad + cols)

                    elif event.key == pygame.K_RETURN and files:
                        self.load_level_file(files[self.currSelectedLoad])
                        self.inChoosingLevel = False
                        self.start_mode = False

                    elif event.key == pygame.K_ESCAPE:
                        self.inChoosingLevel = False

                return  # IMPORTANT: don't process other menu logic

            # ===== MAIN START MENU =====
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.start_state = (self.start_state - 1) % 3

                elif event.key == pygame.K_DOWN:
                    self.start_state = (self.start_state + 1) % 3

                elif event.key == pygame.K_RETURN:
                    # CREATE NEW
                    if self.start_state == 0:
                        self.new_level()

                    # LOAD LEVEL
                    elif self.start_state == 1:
                        self.load_files = self.refresh_load_files()
                        self.currSelectedLoad = 0
                        self.inChoosingLevel = True

                    # BACK TO MAIN MENU
                    elif self.start_state == 2:
                        self.exit_to_menu = True


    def new_level(self):
        # Reset the level to a clean empty level
        self.current_filename = None
        self.level.entityList = []
        self.level_length = max(self.min_length, self.level_length)
        self.input_text = str(self.level_length)
        self.level.level = []
        for y in range(15):
            row = []
            for x in range(self.level_length + 100):
                row.append(Tile(self.level.sprites.spriteCollection.get("sky"), None))
            self.level.level.append(row)
        self.level.levelLength = self.level_length
        self.level_data = {
            "level": {
                "objects": { "bush": [], "cloud": [], "pipe": [], "sky": [], "ground": [] },
                "entities": { "CoinBox": [], "Goomba": [], "Koopa": [], "coin": [], "coinBrick": [], "RandomBox": [] },
                "layers": {
                    "sky": {"x": [0, 200], "y": [0, 13]},
                    "ground": {"x": [0, 200], "y": [13, 15]}
                }
            },
            "length": self.level_length
        }
        self.start_mode = False

    def load_level_file(self, filename):
        try:
            # Load into engine
            self.level.loadLevel(filename)

            # Load JSON for editor state
            with open(f"./levels/{filename}.json") as f:
                data = json.load(f)

                # Normalize and backfill expected structure so older/manual JSON won't break the editor
                level_dict = data.setdefault("level", {})
                objects = level_dict.setdefault("objects", {})
                for k in ("bush", "cloud", "pipe", "sky", "ground"):
                    objects.setdefault(k, [])
                entities = level_dict.setdefault("entities", {})
                for k in ("CoinBox", "Goomba", "Koopa", "coin", "coinBrick", "RandomBox"):
                    entities.setdefault(k, [])
                layers = level_dict.setdefault("layers", {})
                layers.setdefault("sky", {"x": [0, 200], "y": [0, 13]})
                layers.setdefault("ground", {"x": [0, 200], "y": [13, 15]})

                data["length"] = data.get("length", self.level_length)
                self.level_data = data
                self.level_length = data["length"]
                self.input_text = str(self.level_length)

            self.current_filename = filename

        except Exception as e:
            print("Failed to load", filename, e)
            self.input_text = "LOAD FAIL"

        # FIXED MENU STATE
        self.inChoosingLevel = False
        self.start_mode = False


    def chooseLoad(self):
        # set chooser mode and reset selection
        self.inChoosingLevel = True
        self.currSelectedLoad = 0
        # ensure load_files is populated and sorted
        self.load_files = self.refresh_load_files()

    def update(self):
        # exit back to main menu
        if self.exit_to_menu:
            self.exit_to_menu = False
            self.start_mode = True
            self.paused = False
            return

        # PAUSE MODE
        if self.paused:
            self.pause_menu.update()
            return

        # START MENU MODE
        if self.start_mode:
            self.draw_start_menu()
            self.check_start_input()
            pygame.display.update()
            return

        # NORMAL EDITOR MODE
        self.draw_level()
        self.draw_grid()
        self.draw_editor_ui()
        self.check_input()
        pygame.display.update()


    
    def draw_grid(self):
        screen_width, screen_height = self.screen.get_size()
        
        # FULL SCREEN GRID
        for x in range(0, screen_width, 32):
            pygame.draw.line(self.screen, (220, 220, 220), (x, 0), (x, screen_height))
        
        for y in range(0, screen_height, 32):
            pygame.draw.line(self.screen, (220, 220, 220), (0, y), (screen_width, y))
        
        # World Border Line
        limit_pixel_x = (self.level_length * 32)
        screen_x = int(limit_pixel_x - (self.camera_x * 32))
        if 0 <= screen_x <= screen_width+32:
            pygame.draw.line(self.screen, (255, 0, 0), (screen_x, 0), (screen_x, screen_height), 15)
            font = pygame.font.SysFont(None, 24)
            label = font.render("END", True, (255, 0, 0))
            self.screen.blit(label, (screen_x + 5, 10))
    
    def draw_editor_ui(self):
        # 1. "LENGTH:" Label
        self.dashboard.drawText("LENGTH:", 420, 20, 15)

        # 2. Input Box
        if self.input_active: self.current_color = self.color_active
        else: self.current_color = self.color_inactive
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_rec)
        pygame.draw.rect(self.screen, self.current_color, self.input_rec, 2)
        font = pygame.font.SysFont(None, 32)
        text_surface = font.render(self.input_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.input_rec.x+5, self.input_rec.y+5))

        # 3. Ghost Tile
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if not self.input_rec.collidepoint((mouse_x, mouse_y)):
            grid_x = (mouse_x // 32) * 32
            grid_y = (mouse_y // 32) * 32
            
            tool_name = self.tools[self.selected_tool]
            sprite_name = tool_name
            if tool_name == "pipe": sprite_name = "pipeL"
            elif tool_name == "Goomba": sprite_name = "goomba-1"
            elif tool_name == "Koopa": sprite_name = "koopa-1"
            elif tool_name == "coin": sprite_name = "coin"        
            elif tool_name == "CoinBox": sprite_name = "CoinBox"   
            elif tool_name == "coinBrick": sprite_name = "bricks"  

            try:
                sprite_obj = self.level.sprites.spriteCollection.get(sprite_name)
                img = None
                if sprite_obj.image: img = sprite_obj.image.copy()
                elif sprite_obj.animation: img = sprite_obj.animation.images[0].copy()
                
                if img:
                    img.set_alpha(150)
                    offset_y = img.get_height() - 32
                    self.screen.blit(img, (grid_x, grid_y - offset_y))

                    if tool_name == "pipe":
                        for i in range(1, self.pipe_length):
                            body_img = self.level.sprites.spriteCollection.get("pipe2L").image.copy()
                            body_img.set_alpha(150)
                            self.screen.blit(body_img, (grid_x, grid_y + i*32))
            except AttributeError:
                pass


    def check_input(self):
        keys = pygame.key.get_pressed()
        # Rate-limited scrolling when key is held
        if not self.input_active:
            now = pygame.time.get_ticks()
            if keys[pygame.K_RIGHT] and self.camera_x < self.level_length - 10:
                if now - self._last_scroll_time >= self.scroll_interval:
                    self.camera_x = min(self.level_length - 10, self.camera_x + self.camera_step)
                    self._last_scroll_time = now
            if keys[pygame.K_LEFT] and self.camera_x > 0:
                if now - self._last_scroll_time >= self.scroll_interval:
                    self.camera_x = max(0, self.camera_x - self.camera_step)
                    self._last_scroll_time = now
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rec.collidepoint(event.pos):
                    self.input_active = not self.input_active
                else:
                    self.input_active = False
                    self.update_length_from_input()
                    # Left Click -> start placing
                    if event.button == 1:
                        self.placing = True
                        # initialize last place markers to prevent duplicate immediate place
                        mx, my = event.pos
                        gx = (mx // self.grid_size) + int(self.camera_x)
                        gy = my // self.grid_size
                        self._last_place_cell = (gx, gy)
                        self._last_place_time = pygame.time.get_ticks()
                        self.place_object()

            if event.type == pygame.MOUSEBUTTONUP:
                # Stop placing when left button is released
                if event.button == 1:
                    self.placing = False
                    self._last_place_cell = None

            if event.type == pygame.KEYDOWN:
                if self.input_active:
                    if event.key == pygame.K_RETURN:
                        self.update_length_from_input()
                        self.input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        if len(self.input_text) < 5 and event.unicode.isdigit():
                            self.input_text += event.unicode
                else:
                    if event.key == pygame.K_UP:
                        self.selected_tool = (self.selected_tool + 1) % len(self.tools)
                    if event.key == pygame.K_DOWN:
                        self.selected_tool = (self.selected_tool - 1) % len(self.tools)
                    # Toggle Pause
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        self.paused = not self.paused
                        if self.paused:
                            self.draw_level()
                            self.draw_grid()
                            self.draw_editor_ui()
                            pygame.display.update()
                            self.pause_menu.createBackgroundBlur()
                    
                    # Tool Settings
                    current_tool = self.tools[self.selected_tool]
                    if current_tool == "pipe":
                        if event.key == pygame.K_w: self.pipe_length += 1
                        if event.key == pygame.K_s: self.pipe_length = max(2, self.pipe_length - 1)
                    
                    # Save
                    if event.key == pygame.K_F5: self.save_level()
                    
                    # --- NEW: DELETE KEY ---
                    if event.key == pygame.K_DELETE:
                        self.deleting = True
                        self._last_delete_time = pygame.time.get_ticks()
                        self._last_delete_cell = None
                        self.remove_object()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DELETE:
                    self.deleting = False
                    self._last_delete_cell = None

        # Continuous placement while holding left mouse
        if self.placing and not self.input_active:
            now = pygame.time.get_ticks()
            mx, my = pygame.mouse.get_pos()
            if not self.input_rec.collidepoint((mx, my)):
                gx = (mx // self.grid_size) + int(self.camera_x)
                gy = my // self.grid_size
                if (self._last_place_cell != (gx, gy)) or (now - self._last_place_time >= self.place_interval):
                    self.place_object()
                    self._last_place_time = now
                    self._last_place_cell = (gx, gy)
        # Continuous deletion while holding DELETE
        if self.deleting and not self.input_active:
            now = pygame.time.get_ticks()
            mx, my = pygame.mouse.get_pos()
            if not self.input_rec.collidepoint((mx, my)):
                gx = (mx // self.grid_size) + int(self.camera_x)
                gy = my // self.grid_size

                if (self._last_delete_cell != (gx, gy)) or (now - self._last_delete_time >= self.delete_interval):
                    self.remove_object()
                    self._last_delete_time = now
                    self._last_delete_cell = (gx, gy)

    def update_length_from_input(self):
        try:
            length = int(self.input_text)
            if length < self.min_length: length = self.min_length
            self.level_length = length
        except ValueError:
            pass
        self.input_text = str(self.level_length)
        self.level_data["length"] = self.level_length
    
    def draw_level(self):
        # camera_x may be float for smooth scrolling; use ints for tile indices
        start_x = int(self.camera_x)
        end_x = start_x + 21
        
        try:
            for y in range(15):
                for x in range(start_x, end_x):
                    if x < len(self.level.level[y]):
                        tile = self.level.level[y][x]
                        if tile.sprite is not None:
                            if tile.sprite.redrawBackground:
                                self.screen.blit(
                                    self.level.sprites.spriteCollection.get("sky").image,
                                    ((x - start_x) * 32, y * 32),
                                )
                            tile.sprite.drawSprite(x - start_x, y, self.screen)
        except IndexError:
            pass

        for i, entity in enumerate(self.level.entityList):
            # screen_x must be int for blitting and range checks
            screen_x = int(entity.rect.x - (self.camera_x * 32))
            screen_y = int(entity.rect.y)
            
            if -64 < screen_x < 680:
                img = None
                try:
                    if hasattr(entity, 'image') and entity.image:
                        img = entity.image
                    elif hasattr(entity, 'animation') and entity.animation:
                        img = entity.animation.images[0]
                except AttributeError:
                    pass

                if img is None:
                    try:
                        name = entity.__class__.__name__
                        sprite_key = name.lower()
                        if "coinbrick" in sprite_key: sprite_key = "bricks"
                        elif "coinbox" in sprite_key: sprite_key = "CoinBox"
                        elif "coin" in sprite_key: sprite_key = "coin"
                        elif "koopa" in sprite_key: sprite_key = "koopa-1"
                        elif "goomba" in sprite_key: sprite_key = "goomba-1"
                        
                        sprite_obj = self.level.sprites.spriteCollection.get(sprite_key)
                        if sprite_obj.image: img = sprite_obj.image
                        elif sprite_obj.animation: img = sprite_obj.animation.images[0]
                    except AttributeError:
                        pass

                if img:
                    offset_y = img.get_height() - 32
                    self.screen.blit(img, (screen_x, screen_y - offset_y))
                else:
                    pygame.draw.rect(self.screen, (255, 0, 255), (screen_x+5, screen_y+5, 22, 22))
    
    def place_object(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.input_rec.collidepoint((mouse_x, mouse_y)): return

        grid_x = (mouse_x // self.grid_size) + int(self.camera_x)
        grid_y = mouse_y // self.grid_size
        current_tool = self.tools[self.selected_tool]
        for px, py, plen in self.level_data["level"]["objects"]["pipe"]:
            if (px <= grid_x <= px + 1) and (py <= grid_y <= py + plen):
                return # Prevent placing on existing pipe
        # PIPES
        if current_tool == "pipe":
            entry = [grid_x, grid_y, self.pipe_length]
            if entry not in self.level_data["level"]["objects"]["pipe"]:
                self.level_data["level"]["objects"]["pipe"].append(entry)
                self.level.addPipeSprite(grid_x, grid_y, self.pipe_length)

        # ENTITIES
        elif current_tool in ["Goomba", "Koopa", "coin", "CoinBox", "coinBrick"]:
            entry = [grid_x, grid_y]
            json_name = current_tool
            try:
                tile = self.level.level[grid_y][grid_x]
                if tile.sprite and tile.sprite.name == "ground":
                    return
            except:
                pass
            if entry not in self.level_data["level"]["entities"][json_name]:
                self.level_data["level"]["entities"][json_name].append(entry)
                
                if current_tool == "Goomba": 
                    self.level.addGoomba(grid_x, grid_y)
                    self.snap_entity_to_grid(grid_x, grid_y)
                elif current_tool == "Koopa": 
                    self.level.addKoopa(grid_x, grid_y)
                    self.snap_entity_to_grid(grid_x, grid_y)
                elif current_tool == "coin": self.level.addCoin(grid_x, grid_y)
                elif current_tool == "CoinBox": self.level.addCoinBox(grid_x, grid_y)
                elif current_tool == "coinBrick": self.level.addCoinBrick(grid_x, grid_y)
        
        # TILES
        else:
            category = None
            if current_tool == "ground": category = "ground"
            elif current_tool == "sky": category = "sky"
            elif "bush" in current_tool: category = "bush"
            elif "cloud" in current_tool: category = "cloud"

            if category:
                entry = [grid_x, grid_y]
                if entry not in self.level_data["level"]["objects"][category]:
                    self.level_data["level"]["objects"][category].append(entry)

                    if category == "ground":
                        self.level.level[grid_y][grid_x] = Tile(
                            self.level.sprites.spriteCollection.get("ground"),
                            pygame.Rect(grid_x * 32, grid_y * 32, 32, 32)
                        )
                    elif category == "sky":
                        self.level.level[grid_y][grid_x] = Tile(
                            self.level.sprites.spriteCollection.get("sky"), None
                        )
                    elif category == "bush": self.level.addBushSprite(grid_x, grid_y)
                    elif category == "cloud": self.level.addCloudSprite(grid_x, grid_y)

    def snap_entity_to_grid(self, gx, gy):
        try:
            ent = self.level.entityList[-1]
            ent.rect.x = gx * 32
            ent.rect.y = gy * 32
        except: pass

    # --- UPDATED REMOVE FUNCTION ---
    def remove_object(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Ensure grid indices are integers even if camera_x is a float
        grid_x = (mouse_x // 32) + int(self.camera_x)
        grid_y = mouse_y // 32

        # Ensure level structure exists (normalize on the fly)
        level = self.level_data.setdefault("level", {})
        entities = level.setdefault("entities", {})

        # 1. DELETE FROM ENTITIES (CoinBox, coinBrick, coins, mobs)
        for category, entries in list(entities.items()):
            entities[category] = [e for e in entries if not (e[0] == grid_x and e[1] == grid_y)]

        # Visually remove matching entities from entityList (tolerance so clicks are easier)
        self.level.entityList = [
            e for e in self.level.entityList
            if not (abs(e.rect.x - grid_x * 32) < 20 and abs(e.rect.y - grid_y * 32) < 20)
        ]

        # If there was a tile-based entity (CoinBox, coinBrick), clear the tile cell
        try:
            # Safe operation: if it's already sky, this is a no-op
            self.level.level[grid_y][grid_x] = Tile(self.level.sprites.spriteCollection.get("sky"), None)
        except IndexError:
            pass

        # 2. DELETE FROM TILES/OBJECTS
        objects = level.setdefault("objects", {})

        # Pipes (existing logic) — check if click intersects a pipe
        pipes = list(objects.get("pipe", []))
        new_pipes = []
        pipe_deleted = False
        for entry in pipes:
            px, py, plen = entry
            if (px <= grid_x <= px + 1) and (py <= grid_y <= py + plen):
                pipe_deleted = True
                for i in range(plen + 2):
                    try:
                        self.level.level[py + i][px] = Tile(self.level.sprites.spriteCollection.get("sky"), None)
                        self.level.level[py + i][px + 1] = Tile(self.level.sprites.spriteCollection.get("sky"), None)
                    except IndexError:
                        pass
            else:
                new_pipes.append(entry)
        if pipe_deleted:
            objects["pipe"] = new_pipes

        # Bushes (3 tiles wide, 1 high)
        bushes = list(objects.get("bush", []))
        new_bushes = []
        for bx, by in bushes:
            if bx <= grid_x <= bx + 2 and by == grid_y:
                # clear the 3 bush tiles
                for dx in range(3):
                    try:
                        self.level.level[by][bx + dx] = Tile(self.level.sprites.spriteCollection.get("sky"), None)
                    except IndexError:
                        pass
            else:
                new_bushes.append([bx, by])
        objects["bush"] = new_bushes

        # Clouds (3 tiles wide, 2 high)
        clouds = list(objects.get("cloud", []))
        new_clouds = []
        for cx, cy in clouds:
            if cx <= grid_x <= cx + 2 and cy <= grid_y <= cy + 1:
                for dy in range(2):
                    for dx in range(3):
                        try:
                            self.level.level[cy + dy][cx + dx] = Tile(self.level.sprites.spriteCollection.get("sky"), None)
                        except IndexError:
                            pass
            else:
                new_clouds.append([cx, cy])
        objects["cloud"] = new_clouds

        # Ground and Sky (single-tile objects)
        for category in ["ground", "sky"]:
            entries = list(objects.get(category, []))
            before_count = len(entries)
            new_entries = [e for e in entries if not (e[0] == grid_x and e[1] == grid_y)]
            objects[category] = new_entries
            if len(new_entries) < before_count:
                try:
                    self.level.level[grid_y][grid_x] = Tile(
                        self.level.sprites.spriteCollection.get("sky"), None
                    )
                except IndexError:
                    pass

    def save_level(self):
        try:
            os.makedirs("./levels", exist_ok=True)

            #CASE 1: overwrite existing level
            if self.current_filename:
                filename = f"{self.current_filename}.json"

            #CASE 2: new level → generate number
            else:
                files = os.listdir("./levels")
                max_num = 0
                for file in files:
                    if file.startswith("Level1-") and file.endswith(".json"):
                        try:
                            num = int(file.split("-")[1].split(".")[0])
                            if num > max_num:
                                max_num = num
                        except:
                            pass
                filename = f"Level1-{max_num + 1}.json"
                self.current_filename = filename[:-5]  # remember new name

            filepath = f"./levels/{filename}"

            with open(filepath, "w") as outfile:
                json.dump(self.level_data, outfile, indent=4)

            print(f"SAVED: {filename}")
            self.input_text = "SAVED!"

        except Exception as e:
            print("Save failed:", e)



    