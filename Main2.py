from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight, AmbientLight

loadPrcFile('settings.prc')


class PyCraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        Herbe = loader.loadModel("grass-block.glb")
        Herbe.reparentTo(render)
        Terre = loader.loadModel("dirt-block.glb")
        Terre.setPos(0, 4, 0)
        Terre.reparentTo(render)
        Terre = loader.loadModel("dirt-block.glb")
        Terre.setPos(0, 2, 0)
        Terre.reparentTo(render)
        Terre = loader.loadModel("dirt-block.glb")
        Terre.setPos(0, 6, 0)
        Terre.reparentTo(render)
        Terre = loader.loadModel("dirt-block.glb")
        Terre.setPos(0, 8, 0)
        Terre.reparentTo(render)
        Terre = loader.loadModel("dirt-block.glb")
        Terre.setPos(4, 10, 0)
        Terre.reparentTo(render)
        Herbe = loader.loadModel("grass-block.glb")
        Herbe.setPos(6, 0, 0)
        Herbe.reparentTo(render)
        Herbe = loader.loadModel("grass-block.glb")
        Herbe.setPos(0, 12, 0)
        Herbe.reparentTo(render)
        Herbe = loader.loadModel("grass-block.glb")
        Herbe.setPos(4, 8, 0)
        Herbe.reparentTo(render)
        Herbe = loader.loadModel("grass-block.glb")
        Herbe.setPos(6, 10, 0)
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