class Colour:
    def __init__(self, palette):
        self.palette = palette[1:]

    @property
    def red(self):
        return int(self.palette[:2], 16)

    @property
    def green(self):
        return int(self.palette[2:4], 16)

    @property
    def blue(self):
        return int(self.palette[4:], 16)


colour = Colour("#ff0000")
print(colour.red)
print(colour.green)
print(colour.blue)