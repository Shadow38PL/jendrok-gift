from pygame import Color

from model import Model
from texture import Texture
from vector2 import Vector2Float


class Widget:
    position: Vector2Float
    size: Vector2Float
    background: Color
    texture: Texture
    text: str
    children = None
    onClick = None
    updated = True

    def __init__(self, position: Vector2Float, size: Vector2Float, background: Color, texture: Texture, text: str, onclick):
        self.position = position
        self.size = size
        self.background = background
        self.texture = texture
        self.text = text
        self.onClick = onclick
        self.children = []

    def animate(self, deltaTime: float):
        for child in self.children:
            child.animate(deltaTime)

    def setText(self, text: str):
        self.text = text
        self.updated = True

    def click(self, clickPosition: Vector2Float) -> bool:
        if clickPosition is not None:
            for child in self.children:
                if child.click(clickPosition):
                    return True

            if self.onClick is not None and self.position.x <= clickPosition.x <= (self.position.x + self.size.x) and \
                    self.position.y <= clickPosition.y <= (self.position.y + self.size.y):
                self.onClick()

    def model(self) -> Model:
        updated = self.updated
        self.updated = False
        return Model(self.position, self.size, self.background, self.texture, self.text, 0, updated, True)
