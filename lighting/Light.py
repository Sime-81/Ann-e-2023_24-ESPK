from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight, AmbientLight

loadPrcFile('../settings.prc')


class PyCraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        Herbe = loader.loadModel("../grass-block.glb")
        Herbe.reparentTo(render)

        mainLight = DirectionalLight('main light')
        mainLightNodePath = render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        render.setLight(mainLightNodePath)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor((0.3, 0.3, 0.3, 1))
        ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNodePath)


game = PyCraft()
game.run()