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
from config import Config

def runGame(config = Config()):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(config.name)
    screen = pygame.display.set_mode(config.resolution)
    while True:
        clock.tick(config.fps/60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        screen.fill(config.bg_color)
        pygame.display.flip()
    #clock = pygame.time.Clock()
    #pygame.display.update()