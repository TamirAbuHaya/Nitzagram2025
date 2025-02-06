import pygame

from constants import *
from helpers import screen
from Post import Post



class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color


    def display(self):
        # background fill

        # show text

        super().display()

