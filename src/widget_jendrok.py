import math

from model import Model
from widget import Widget


class WidgetJendrok(Widget):
    rotation = 0.0
    time = 0.0
    spinTimer = 0.0
    spinning = False

    def __init__(self, position, size, background, texture, text, onclick):
        super().__init__(position, size, background, texture, text, onclick)

    def animate(self, deltaTime: float):
        super().animate(deltaTime)

        if not self.spinning:
            self.time += deltaTime
            self.rotation = math.sin(self.time) * 90 - 45
        else:
            self.spinTimer += deltaTime
            self.rotation += 2 * math.pi / self.spinTimer

            if self.spinTimer >= 1:
                self.spinTimer = 0
                self.spinning = False

    def spin(self):
        self.spinning = True

    def model(self) -> Model:
        return Model(self.position, self.size, self.background, self.texture, self.text, self.rotation, True, False)
