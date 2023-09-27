import keyboard
from mcpi.minecraft import Minecraft

class Wall:
    def __init__(self, pos, rotated=False, material_id="Default:stone", Width=5, height=5):
        self.mc = Minecraft.create()
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.Width = Width
        self.height = height

    def build(self):
        x, y, z = self.pos
        material_id = self.mc.getBlockWithData(x, y, z).id
        if self.rotated:
            for i in range(self.height):
                for j in range(self.Width):
                    self.mc.setBlock(x + j, y, z + i, material_id)
        else:
            for i in range(self.Width):
                for j in range(self.height):
                    self.mc.setBlock(x + i, y, z + j, material_id)

def execAufgabe2():
    mc = Minecraft.create(address="localhost", port=4711)
    player_pos = mc.player.getPos()
    print("Mit Server verbunden. Warte auf Input...")
    # Erstelle eine gedrehte Wand
    rotated_wall = Wall((player_pos.x, player_pos.y, player_pos.z), rotated=True, material_id="minecraft:stone", Width=5, height=5)

    keyboard.on_press_key('b', lambda e: rotated_wall.build())

    # Halte das Programm am Laufen
    keyboard.wait()
    
execAufgabe2()
