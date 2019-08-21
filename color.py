class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, red, green, blue):
        self.set_rgb(red, green, blue)

    def set_rgb(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def set_hex(self, hexa):
        print "HEX: #" + hexa

    def to_string(self):
        return self.red + ", " + self.green + ", " + self.blue

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue
