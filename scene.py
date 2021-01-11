from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

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

        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        #self.camera.setPos(0, 0, 256)

        
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont