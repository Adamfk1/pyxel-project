from interface import Interface
import pyxel

interface = Interface(255,255)


pyxel.init(interface.width, interface.height, caption="Super Mario")

pyxel.load("assets/marioassets.pyxres")

pyxel.run(interface.update, interface.draw)