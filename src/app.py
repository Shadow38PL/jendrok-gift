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
    "Chłopaki, ale mam \npomysła na biznes",
    "Jeszcze miesiąc i będziemy \nzarabiać",
    "głupie i bez sensu",
    "Naprawdę musimy zaplanować\ndalszy rozwój Heseya",
    "nigdy heseya nie będzie \nmiała logo",
    "Kolektyw programistyczny Heseya",
    "teraz to się nazywa \nheseya ciągły rozwój",
    "Zamykamy firmę, chcesz premie\nza acata czy nie",
    "to za tą kasę zamykamy heseya",
    "Zamykamy tą heseje w pizdu",
    "dokańczamy ft i komiksy\nzamykamy spółkę",
    "a chuj mi w dupe",
    "ale nintendo \nto jest pojebane z cenami",
    "a pierdolne sobie \nskrypciki pojebane",
    "bardziej pojebane \nniż rework bazy danych",
    "chińskie bajki to \nzawsze pojebane xd",
    "Zamknijmy to wszystko w pizdu",
    "Kup puki jest kasa xd",
    "że kasa z acata idzie \nna bierzące a ja chce moje 125zł",
    "JESTEŚMY BOGACI",
    "tak to jest jak \nbackend siada do frontu",
    "huj wam w dupe \npaweł was oszukał",
    "Paweł dzwonił że chce wrócić",
    "ale ten paweł to kozak",
    "Idziesz do sądu mówisz, Paweł jest \nbe, a Paweł grzecznie płaci",
    "Dzwonię. Paweł nie odbiera",
    "paweł dzwonił i coś tam\nfaflunił o 400tys dotacji",
    "paweł to jest pajac"
]


def main():
    pygame.init()
    pygame.display.set_caption("Jendrok")
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    currentText = [""]

    def close():
        pygame.quit()
        sys.exit(0)

    def getQuote():
        return "\"" + quotes[random.randint(0, quotes.__len__() - 1)] + "\""

    def generateQuote():
        newText = getQuote()
        while currentText[0] == newText:
            newText = getQuote()
        return newText

    def showQuote():
        currentText[0] = generateQuote()
        splittedText = currentText[0].split("\n")
        text.text = splittedText[0]
        text2.text = splittedText[1] if len(splittedText) > 1 else ""


    title1 = Widget(Vector2Float(220, 40), Vector2Float(320, 32), None, None, "Jendrok MOOD", None)
    title2 = Widget(Vector2Float(220, 70), Vector2Float(320, 32), None, None, "Generator", None)
    jendrok = WidgetJendrok(Vector2Float(20, 20), Vector2Float(120, 168), None, Texture.JENDROK, None, None)
    text = Widget(Vector2Float(14, 210), Vector2Float(450, 32), None, None, "", None)
    text2 = Widget(Vector2Float(24, 235), Vector2Float(450, 32), None, None, "", None)
    decor = Widget(Vector2Float(0, 280), Vector2Float(480, 40), Color(143, 2, 44), None, None, None)
    exit = Widget(Vector2Float(444, 4), Vector2Float(32, 32), None, Texture.EXIT, None, close)

    showQuote()

    def onclick():
        showQuote()
        jendrok.spin()

    root = Widget(Vector2Float(0, 0), Vector2Float(WIDTH, HEIGHT), Color(255, 255, 255), None, None, onclick)
    root.children.append(title1)
    root.children.append(title2)
    root.children.append(jendrok)
    root.children.append(text)
    root.children.append(text2)
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

        deltaTime = clock.tick(16) / 1000.0
        root.animate(deltaTime)
        root.click(clickPosition)

        renderer.render(root)


if __name__ == '__main__':
    main()
