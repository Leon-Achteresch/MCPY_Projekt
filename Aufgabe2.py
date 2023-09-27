import keyboard
from mcpi.minecraft import Minecraft

class Wall:
    def __init__(self, pos, rotated=False, material_id="Default:stone", Width=5, height=5):
        self.__mc = Minecraft.create()
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.Width = Width
        self.height = height

    def build(self):
        print('build')
        x, y, z = self.pos
        if self.rotated:
            for i in range(self.height):
                for j in range(self.Width):
                    self.__mc.setBlock(x + j, y + i, z, self.material_id)
        else:
            for i in range(self.Width):
                for j in range(self.height):
                    self.__mc.setBlock(x, y + i, z + j, self.material_id)

def execAufgabe2():
    def build():
        player_pos = mc.player.getPos()
        rotated_wall = Wall((player_pos.x +1 , player_pos.y, player_pos.z), rotated=True, material_id=1, Width=5, height=5)
        rotated_wall.build()
        not_rotated_wall = Wall((player_pos.x, player_pos.y, player_pos.z +1), rotated=False, material_id=1, Width=5, height=5)
        not_rotated_wall.build()

    mc = Minecraft.create(address="localhost", port=4711)
    
    mc.postToChat("Warte auf input...")
    print("Mit Server verbunden. Warte auf Input...")
    # Erstelle eine gedrehte Wand
    
    
    keyboard.on_press_key('b', lambda e: build())

    # Halte das Programm am Laufen
    keyboard.wait()
    
execAufgabe2()
