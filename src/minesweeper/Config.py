
from ctypes.wintypes import RGB

class Config:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = RGB(0, 0, 0)
        self.fps = 60