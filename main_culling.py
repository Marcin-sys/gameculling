
from direct.showbase.ShowBase import ShowBase
# base = ShowBase()
from panda3d.core import *

from direct.task import Task
from direct.actor.Actor import Actor
# import direct.directbase.DirectStart

loadPrcFileData("", "load-file-type p3assimp")  #here check

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        # Load Model Teapot to scene
        self.teapot = self.loader.load_model("models/teapot_n_glass.obj")
        self.teapot.reparentTo(self.render)
        self.teapot.setPos(-10, 6, 0)
        self.teapot.setHpr(0, 90, 320)
        self.teapot.setColor(1, 0.6, 0.8, 0.7)

        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the CameraTask procedure to the task manager.
        self.taskMgr.add(self.CameraTask, "CameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")


    # Define a procedure to move the camera.
    def CameraTask(self, task):
        # sets the position of the camera
        self.camera.setPos(8 , -10,  6)
        # sets the orientation
        self.camera.setHpr(40, -20, 0)
        return Task.cont

app = MyApp()
app.run()
