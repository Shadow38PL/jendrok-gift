import pygame
import sys

from pygame import Color

from renderer import Renderer
from texture import Texture
from vector2 import Vector2Float
from widget import Widget

HEIGHT = 320
WIDTH = 480


def main():
    pygame.init()
    pygame.display.set_caption("Jendrok")
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    def close():
        pygame.quit()
        sys.exit(0)

    pacman = Widget(Vector2Float(20, 20), Vector2Float(32, 32), None, Texture.PACMAN_0, None, close)
    text = Widget(Vector2Float(20, 70), Vector2Float(320, 32), None, None, "Ale kupa", None)

    def onclick():
        text.text = "lol xd haha"

    root = Widget(Vector2Float(0, 0), Vector2Float(WIDTH, HEIGHT), Color(255, 255, 255), None, None, onclick)


    root.children.append(pacman)
    root.children.append(text)

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
