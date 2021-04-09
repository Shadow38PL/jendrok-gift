import pygame
from pygame import Rect
from pygame.font import Font

from widget import Widget

BACKGROUND = (0, 0, 0)


class Renderer:
    display: pygame.display
    font: Font

    def __init__(self, display: pygame.display):
        self.display = display
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)

    def renderWidget(self, widget: Widget):
        model = widget.model()

        if model.background is not None:
            self.display.fill(model.background, Rect(
                model.position.x,
                model.position.y,
                model.size.x,
                model.size.y
            ))

        if model.texture is not None:
            texture = pygame.transform.scale(model.texture.value, (model.size.x, model.size.y))
            self.display.blit(texture, (model.position.x, model.position.y))

        if model.texture is not None:
            texture = pygame.transform.scale(model.texture.value, (model.size.x, model.size.y))
            self.display.blit(texture, (model.position.x, model.position.y))

        if model.text is not None:
            text = self.font.render(model.text, True, (0, 0, 0))
            self.display.blit(text, (model.position.x, model.position.y), Rect(
                0,
                0,
                model.size.x,
                model.size.y
            ))

        for child in widget.children:
            self.renderWidget(child)

    def render(self, widget: Widget):
        self.display.fill(BACKGROUND)
        self.renderWidget(widget)
        pygame.display.update()
