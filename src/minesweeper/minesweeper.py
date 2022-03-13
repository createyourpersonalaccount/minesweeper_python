# Copyright (C) 2022  Nikolaos Chatzikonstantinou <nchatz314@gmail.com>
# Copyright (C) 2022  Nikolaos Zevgolis <nzevgolisda@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import pygame
from config import gameConfig

from ctypes.wintypes import RGB




def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    config = Config()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    #Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill(config.bg_color)
        #Make the most recently drawn screen visible
        pygame.display.flip()
run_game()