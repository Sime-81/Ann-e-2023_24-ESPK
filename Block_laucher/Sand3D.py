from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

loadPrcFile('../settings.prc')


class MyBlock(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        Herbe = loader.loadModel("../sand-block.glb")
        Herbe.reparentTo(render)


game = MyBlock()
game.run()