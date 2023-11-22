from mcpi.minecraft import Minecraft
import keyboard
import random

class House:
    def __init__(self, pos, bw: Minecraft, wallFront, wallLeft, wallBack, wallRight, roof):
        self.__mc: Minecraft = bw
        self.pos = pos
        self.wallFront :WallWithDoor    = wallFront
        self.wallLeft  :WallWithWindow  = wallLeft
        self.wallBack  :Wall            = wallBack
        self.WallRight :WallWithWindow  = wallRight
        self.roof      :Roof   = roof

    def build(self):
        print('build')
        self.__mc.postToChat('building House')
        x, y, z = self.pos
        self.roof.build()
        self.wallFront.build()
        self.wallLeft.build()
        self.wallBack.build()
        self.WallRight.build()

    def change_wall_material(self, new_materail_id):
        self.wallFront.material_id = new_materail_id
        self.wallLeft.material_id = new_materail_id
        self.wallBack.material_id = new_materail_id
        self.WallRight.material_id = new_materail_id

class Roof:
    def __init__(self, pos, bw: Minecraft, roof_material_id=45, width=6, depth=6):
        self.__mc: Minecraft = bw
        self.pos = pos
        self.roof_material_id = roof_material_id
        self.width = width
        self.depth = depth

    def build(self):
        print('build')
        self.__mc.postToChat('building Roof')
        x, y, z = self.pos
        self.__mc.setBlocks(x +1,y,z +1,x + self.width, y, z + self.depth, self.roof_material_id)

class Wall:
    def __init__(self, pos, bw:Minecraft, rotated=False, material_id="Default:stone", width=6, height=6):
        self._mc:Minecraft = bw
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.width = width
        self.height = height

    def build(self):
        print('build')
        self._mc.postToChat('building Wall')
        x, y, z = self.pos
        if self.rotated:
            for i in range(self.height):
                for j in range(self.width):
                    self._mc.setBlock(x +1 + j, y + i, z+1, self.material_id)
        else:
            for i in range(self.width):
                for j in range(self.height):
                    self._mc.setBlock(x+1, y + i, z +1 + j, self.material_id)

class WallWithDoor(Wall):
    def __init__(self, pos, bw: Minecraft, rotated=False, material_id="Default:stone", width=6, height=6, door_material="air"):
        super().__init__(pos, bw, rotated, material_id, width, height)
        self.door_material = door_material
    
    def build(self):
        super().build()
        self._mc.postToChat('building WallWithDoor')
        x, y, z = self.pos
        if self.rotated:
            self._mc.setBlocks(x + 1 +1 , y, z+1 +1, x + self.width - 1, y + 1 + self.height, z - 1, 0)
        else:
            self._mc.setBlocks(x + 1, y +1, z+3, x + 1, y + 3, z + 4, 0)

class WallWithWindow(Wall):
    def __init__(self, pos, bw: Minecraft, rotated=False, material_id="Default:stone", width=6, height=6, window_material="air"):
        super().__init__(pos, bw, rotated, material_id, width, height)
        self.window_material = window_material
    
    def build(self):
        super().build()
        self._mc.postToChat('building WallWithWindow')
        x, y, z = self.pos
        if self.rotated:
            self._mc.setBlocks(x+2, y + 1, z + 1, x + self.width - 1, y + self.height- 2, z+1, 95)
        else:
            self._mc.setBlocks(x + 1, y +1, z+1 +1, x + 1, y + 3, z + 3, 0)

def execAufgabe6():
    def build(mc:Minecraft):
        player_pos = mc.player.getPos()
        wallFront   = WallWithDoor((player_pos.x , player_pos.y, player_pos.z), rotated=False, material_id=1, width=6, height=6, bw = mc, door_material="air")
        wallLeft    = WallWithWindow((player_pos.x , player_pos.y, player_pos.z), rotated=True, material_id=1, width=6, height=6, bw = mc, window_material="air")
        wallBack    = Wall((player_pos.x + 5 , player_pos.y, player_pos.z), rotated=False, material_id=1, width=6, height=6, bw = mc)
        wallRight   = WallWithWindow((player_pos.x , player_pos.y, player_pos.z + 5), rotated=True, material_id=1, width=6, height=6, bw = mc, window_material="air")
        roof        = Roof(pos=(player_pos.x , player_pos.y +6, player_pos.z), roof_material_id=45, width=6, depth=6, bw = mc)
        
        house = House(pos=(player_pos.x , player_pos.y +6, player_pos.z), wallFront=wallFront, wallLeft=wallLeft, wallBack=wallBack, wallRight=wallRight, roof=roof, bw=mc)
        house.change_wall_material(random.randint(1, 100))
        house.build()
        
        

    mc = Minecraft.create(address="10.1.48.81", port=4711)
    
    mc.postToChat("Warte auf input...")
    print("Mit Server verbunden. Warte auf Input...")   
    
    keyboard.on_press_key('b', lambda e: build(mc))
    # Halte das Programm am Laufen
    keyboard.wait()
    
execAufgabe6()
        