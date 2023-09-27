import keyboard
from mcpi.minecraft import Minecraft

class Wall:
    def __init__(self, pos, bw:Minecraft, rotated=False, material_id="Default:stone", width=5, height=5):
        self.__mc:Minecraft = bw
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.width = width
        self.height = height

    def build(self):
        print('build')
        self.__mc.postToChat('building')
        x, y, z = self.pos
        if self.rotated:
            for i in range(self.height):
                for j in range(self.width):
                    self.__mc.setBlock(x +1 + j, y + i, z, self.material_id)
        else:
            for i in range(self.width):
                for j in range(self.height):
                    self.__mc.setBlock(x, y + i, z +1 + j, self.material_id)

def execAufgabe2():
    def build(mc:Minecraft):
        player_pos = mc.player.getPos()
        wall = Wall((player_pos.x , player_pos.y, player_pos.z), rotated=True, material_id=1, width=5, height=5, bw = mc)
        wall.build()
        wall.rotated=False
        wall.build()
        

    mc = Minecraft.create(address="localhost", port=4711)
    
    mc.postToChat("Warte auf input...")
    print("Mit Server verbunden. Warte auf Input...")
    # Erstelle eine gedrehte Wand
    
    
    keyboard.on_press_key('b', lambda e: build(mc))

    # Halte das Programm am Laufen
    keyboard.wait()
    
execAufgabe2()
