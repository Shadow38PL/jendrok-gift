import pygame
import sys
import random

from pygame import Color

from renderer import Renderer
from texture import Texture
from vector2 import Vector2Float
from widget import Widget
from widget_jendrok import WidgetJendrok

HEIGHT = 320
WIDTH = 480

quotes = [
    "dron.on... dron OFF hyhyHY",
    "Bartek NIE DZIAŁAAAAAAAAAAA",
    "lol",
    "kek",
    "xd"
]


def main():
    pygame.init()
    pygame.display.set_caption("Jendrok")
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    def close():
        pygame.quit()
        sys.exit(0)

    title1 = Widget(Vector2Float(190, 40), Vector2Float(260, 32), None, None, "Jendrok MOOD", None)
    title2 = Widget(Vector2Float(190, 70), Vector2Float(260, 32), None, None, "Simulator", None)
    jendrok = WidgetJendrok(Vector2Float(20, 20), Vector2Float(100, 148), None, Texture.JENDROK, None, None)
    text = Widget(Vector2Float(20, 220), Vector2Float(440, 32), None, None, quotes[random.randint(0, quotes.__len__() - 1)], None)
    decor = Widget(Vector2Float(0, 280), Vector2Float(480, 40), Color(143, 2, 44), None, None, None)
    exit = Widget(Vector2Float(440, 0), Vector2Float(40, 40), None, Texture.JENDROK, None, close)

    def onclick():
        newText = quotes[random.randint(0, quotes.__len__() - 1)]
        while text.text == newText:
            newText = quotes[random.randint(0, quotes.__len__() - 1)]
        text.text = newText
        jendrok.spin()

    root = Widget(Vector2Float(0, 0), Vector2Float(WIDTH, HEIGHT), Color(255, 255, 255), None, None, onclick)
    root.children.append(title1)
    root.children.append(title2)
    root.children.append(jendrok)
    root.children.append(text)
    root.children.append(decor)
    root.children.append(exit)

    while True:
        clickPosition: Vector2Float = None

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clickPosition = Vector2Float(pos[0], pos[1])

        deltaTime = clock.tick(60) / 1000.0
        root.animate(deltaTime)
        root.click(clickPosition)

        renderer.render(root)


if __name__ == '__main__':
    main()
