
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
# import direct.directbase.DirectStart
# from panda3d.core import *


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
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
