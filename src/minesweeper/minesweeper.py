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
from config import Config
from __init__ import runGame

config = Config()
runGame(config)
"""This should be in a function called runGame that takes as argument a configuration class 
that contains the window size. """

"""Use clock.tick() to set the framerate to 60 fps. See the pygame example https://github.com/pygame/pygame/blob/main/examples/chimp.py as well."""

