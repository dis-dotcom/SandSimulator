from pygame import Color


class Config:
    def __init__(self):
        self.text_size = 20
        self.text_color = Color(0, 0, 0)

        self.canvas_size = 500, 500
        self.background_color = Color(255, 255, 255)

    background_color = Color(255, 255, 255)
    text_color = Color(0, 0, 0)
    text_size = 20
    canvas_size = 500, 500