from mcpi.minecraft import Minecraft
import keyboard

class Wall:
    def __init__(self, pos, bw: Minecraft, rotated=False, material_id=4, width=6, height=6):
        self._mc: Minecraft = bw
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.width = width
        self.height = height

    def build(self):
        print('build')
        self._mc.postToChat('building')
        x, y, z = self.pos
        # self.__mc.postToChat(self.pos)
        if self.rotated:
            for i in range(self.height):
                for j in range(self.width):
                    self._mc.setBlock(x + j, y + i, z, self.material_id)
        else:
            for i in range(self.width):
                for j in range(self.height):
                    self._mc.setBlock(x, y + i, z + j, self.material_id)

class WallWithDoor(Wall):
    def __init__(self, pos, bw: Minecraft, door_material_id=324):
        # self.__mc: Minecraft = bw
        super().__init__(pos, bw, True)
        self.door_material_id = door_material_id

    def build(self):
        super().build()
        x, y, z = self.pos
        door_x = x + self.width // 2
        door_z = z + self.height // 3
        for i in range(2):
            for j in range(3):
                self._mc.setBlock(door_x + i - 1, y + j, door_z - 2, self.door_material_id)


class WallWithWindow(Wall):
    def __init__(self, pos, bw: Minecraft, window_material_id=95):
        # self.__mc: Minecraft = bw
        super().__init__(pos, bw)
        self.window_material_id = window_material_id

    def build(self):
        
        super().build()
        x, y, z = self.pos
        window_x = x + self.width  // 3
        window_z = z + self.height // 2
        for i in range(2):
            for j in range(2):
                self._mc.setBlock(window_x- 2, y + j + 1, window_z + i -1 , self.window_material_id)

mc = Minecraft.create(address="localhost", port=4711)

def place_four_walls_near_player(x, y, z):
    for i in range(2):
        wall = WallWithDoor((x, y, z + (i*5)), mc, door_material_id=0)
        wall2 = WallWithWindow((x + (i*5), y, z ), mc, window_material_id=20)
        wall.build()
        wall2.build()

def main():
    x, y, z = mc.player.getPos()
    place_four_walls_near_player(x, y, z)

def execAufgabe4():
    mc.postToChat("Warte auf Input...")
    print("Mit Server verbunden. Warte auf Input...")

    keyboard.on_press_key('b', lambda e: main())

    keyboard.wait()

execAufgabe4()
