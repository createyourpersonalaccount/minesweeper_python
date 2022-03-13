use clock = pygame.time.Clock() in runGame together with clock.tick(config.FPS).

In src/minesweeper/minesweeper.py:

> @@ -12,3 +12,30 @@
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
+
+import sys
+import pygame
+from Config import Config
+from ctypes.wintypes import RGB
+
+def runGame():
+    '''This should be in a function called runGame that takes as argument a configuration class 
+    that contains the window size. Use clock.tick() to set the framerate to 60 fps.
+    See the pygame example https://github.com/pygame/pygame/blob/main/examples/chimp.py as well.'''
+
+    pygame.init()
+    pygame.display.set_caption("Minesweeper")
The string "Minesweeper" should be part of the configuration.

In src/minesweeper/minesweeper.py:

> @@ -12,3 +12,30 @@
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
+
+import sys
+import pygame
+from Config import Config
+from ctypes.wintypes import RGB
+
+def runGame():
+    '''This should be in a function called runGame that takes as argument a configuration class 
+    that contains the window size. Use clock.tick() to set the framerate to 60 fps.
+    See the pygame example https://github.com/pygame/pygame/blob/main/examples/chimp.py as well.'''
+
+    pygame.init()
+    pygame.display.set_caption("Minesweeper")
+    config = Config()
config should be an argument of runGame, and the initialization should happen at __init__.py.

In src/minesweeper/minesweeper.py:

> +
+    pygame.init()
+    pygame.display.set_caption("Minesweeper")
+    config = Config()
+    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
+    #Start the main loop for the game.
+    while True:
+        #Watch for keyboard and mouse events.
+        for event in pygame.event.get():
+            if event.type == pygame.QUIT:
+                sys.exit()
+        #Redraw the screen during each pass through the loop.
+        screen.fill(config.bg_color)
+        #Make the most recently drawn screen visible
+        pygame.display.flip()
+        print(config.clock.tick(1))
Don't print the result, and change the line as explained above.

In src/minesweeper/minesweeper.py:

> +def runGame():
+    '''This should be in a function called runGame that takes as argument a configuration class 
+    that contains the window size. Use clock.tick() to set the framerate to 60 fps.
+    See the pygame example https://github.com/pygame/pygame/blob/main/examples/chimp.py as well.'''
+
+    pygame.init()
+    pygame.display.set_caption("Minesweeper")
+    config = Config()
+    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
+    #Start the main loop for the game.
+    while True:
+        #Watch for keyboard and mouse events.
+        for event in pygame.event.get():
+            if event.type == pygame.QUIT:
+                sys.exit()
+        #Redraw the screen during each pass through the loop.
This comment is not necessary, please remove.

In src/minesweeper/minesweeper.py:

> +    that contains the window size. Use clock.tick() to set the framerate to 60 fps.
+    See the pygame example https://github.com/pygame/pygame/blob/main/examples/chimp.py as well.'''
+
+    pygame.init()
+    pygame.display.set_caption("Minesweeper")
+    config = Config()
+    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
+    #Start the main loop for the game.
+    while True:
+        #Watch for keyboard and mouse events.
+        for event in pygame.event.get():
+            if event.type == pygame.QUIT:
+                sys.exit()
+        #Redraw the screen during each pass through the loop.
+        screen.fill(config.bg_color)
+        #Make the most recently drawn screen visible
This comment is not necessary, please remove.

In src/minesweeper/Config.py:

> @@ -0,0 +1,10 @@
+
+import pygame
+from ctypes.wintypes import RGB
+
+class Config:
