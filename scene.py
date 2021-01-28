import yaml
from math import pi, sin, cos
from panda3d.core import KeyboardButton, LVector2f
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

FLOOR_CONTROL = config['floor_control']
SPEED = config['speed']

class PyramidRender(ShowBase):
    def __init__(self, squares):
        ShowBase.__init__(self)
        wireframe = self.render.attachNewNode("wireframe")
        for square in squares:
            pyramid = self.loader.loadModel("model/pyramid")
            pyramid.reparentTo(self.render)
            pyramid.setPos(square.x * 2 + square.size, square.y * 2 + square.size, 0)
            pyramid.setScale(square.size)
            pyramid.setColor(1, 1, 1, 1)
            wired_pyramid = pyramid.copyTo(wireframe)
            wired_pyramid.setColor(1, 0, 1, 1)
            wired_pyramid.setRenderModeWireframe()

        if (FLOOR_CONTROL):
            base.disableMouse()
            self.taskMgr.add(self.key_task, "key_task")
            self.camera.setPos(0, 0, 2)
        
    def key_task(self, task):
        is_down = self.mouseWatcherNode.is_button_down
        [x, y, z] = self.camera.getPos()
        [h, p, r] = self.camera.getHpr()
        radian = h * (pi / 180.0)
        pos_x = sin(radian)
        pos_y = cos(radian) 

        [dx, dy, dz, dh, dp, dr] = [0 for x in range(6)]
        if is_down(KeyboardButton.asciiKey('w')):
            dx += -pos_x
            dy += pos_y
        elif is_down(KeyboardButton.asciiKey('s')):
            dx += pos_x
            dy += -pos_y

        if is_down(KeyboardButton.asciiKey('d')):
            dx += pos_y
            dy += pos_x
        elif is_down(KeyboardButton.asciiKey('a')):
            dx += -pos_y
            dy += -pos_x

        if is_down(KeyboardButton.asciiKey('q')):
            dh += SPEED * 2
        elif is_down(KeyboardButton.asciiKey('e')):
            dh += -SPEED * 2

        if is_down(KeyboardButton.space()):
            dz += SPEED
        elif is_down(KeyboardButton.shift()):
            if (z > 2):
                dz += -SPEED

        if is_down(KeyboardButton.asciiKey('r')):
            dp += SPEED
        elif is_down(KeyboardButton.asciiKey('f')):
            dp += -SPEED

        if is_down(KeyboardButton.enter()):
            z = 0
            dz = 0

        dxdy = LVector2f(dx, dy)
        dxdy = dxdy.normalized() * SPEED
        [dx, dy] = dxdy
        self.camera.setPosHpr(x + dx, y + dy, z + dz, h + dh, p + dp, r + dr)
        return Task.cont