import pygame
from pygame import Rect
from pygame.font import Font

from texture import Texture
from widget import Widget

BACKGROUND = (255, 255, 255)


class Renderer:
    display: pygame.display
    font: Font
    experimental = True

    def __init__(self, display: pygame.display):
        self.display = display
        self.font = pygame.font.Font('./fonts/Montserrat-SemiBold.ttf', 24)
        self.display.fill(BACKGROUND)

    def renderWidget(self, widget: Widget):
        model = widget.model()

        if model.updated or model.background == BACKGROUND:
            if model.texture is Texture.JENDROK:
                self.display.fill(BACKGROUND, Rect(
                    0,
                    0,
                    220,
                    215
                ))
            else:
                self.display.fill(BACKGROUND, Rect(
                    model.position.x,
                    model.position.y,
                    model.size.x,
                    model.size.y
                ))

            if model.background is not None:
                self.display.fill(model.background, Rect(
                    model.position.x,
                    model.position.y,
                    model.size.x,
                    model.size.y
                ))

            if model.texture is not None:
                texture = pygame.transform.scale(model.texture.value, (model.size.x, model.size.y))
                texture = pygame.transform.rotate(texture, model.rotation)
                self.display.blit(texture, (model.position.x, model.position.y))

            if model.text is not None:
                text = self.font.render(model.text, True, (51, 51, 51))
                self.display.blit(text, (model.position.x, model.position.y), Rect(
                    0,
                    0,
                    model.size.x,
                    model.size.y
                ))

            if self.experimental:
                if model.texture is Texture.JENDROK:
                    pygame.display.update(Rect(
                        0,
                        0,
                        220,
                        215
                    ))
                else:
                    pygame.display.update(Rect(
                        model.position.x,
                        model.position.y,
                        model.size.x,
                        model.size.y
                    ))

        for child in widget.children:
            self.renderWidget(child)

    def render(self, widget: Widget):
        self.renderWidget(widget)
        if not self.experimental:
            pygame.display.update()
