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

import pygame

class gameConfig:
    def __init__(self):
        self.fps = 60
        self.screen_width = 600
        self.screen_height = 400
        self.screen_resolution = (self.screen_width, self.screen_height)
        self.bg_color = pygame.Color(100, 100, 100)
        self.clock = pygame.time.Clock()
        self.name = "Minesweeper"
