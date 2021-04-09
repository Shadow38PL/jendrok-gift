from pygame import Color

from texture import Texture
from vector2 import Vector2Float


class Model:
    background: Color
    texture: Texture
    position: Vector2Float
    size: Vector2Float
    rotation: float
    text: str

    def __init__(self, position: Vector2Float, size: Vector2Float, background: Color, texture: Texture, text: str, rotation: float):
        self.position = position
        self.size = size
        self.background = background
        self.texture = texture
        self.text = text
        self.rotation = rotation
