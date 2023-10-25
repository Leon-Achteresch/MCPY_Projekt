from mcpi.minecraft import Minecraft
import keyboard

class Roof:
    def __init__(self, pos, bw: Minecraft, roof_material_id=45, width=6, depth=6):
        self.__mc: Minecraft = bw
        self.pos = pos
        self.material_id = roof_material_id
        self.width = width
        self.depth = depth

    def build(self):
        print('build')
        self.__mc.postToChat('building')
        x, y, z = self.pos
        self.__mc.setBlocks(x +1,y,z +1,x + self.width +1, y, z + self.depth +1, self.material_id)

def execAufgabe5():
    def build(mc:Minecraft):
        player_pos = mc.player.getPos()
        roof = Roof(pos=(player_pos.x , player_pos.y, player_pos.z), roof_material_id=45, width=6, depth=6, bw = mc)
        roof.build()
        

    mc = Minecraft.create(address="10.1.48.68", port=4711)
    
    mc.postToChat("Warte auf input...")
    print("Mit Server verbunden. Warte auf Input...")   
    
    keyboard.on_press_key('b', lambda e: build(mc))

    # Halte das Programm am Laufen
    keyboard.wait()
    
execAufgabe5()

# Aggregation:
# Aggregation ist eine Beziehung zwischen einem ganzen Objekt (Teilhaber) und seinen Teilen.
# Das bedeutet, dass ein Teilobjekt unabhängig vom ganzen Objekt existieren kann,
# und es kann auch in Beziehung zu anderen Objekten stehen.
# Das ganze Objekt ist jedoch für die Lebensdauer seiner Teile verantwortlich.
# Ein klassisches Beispiel für Aggregation ist die Beziehung zwischen einem Auto und seinen Rädern.
# Die Räder können von verschiedenen Autos verwendet werden, und sie können auch unabhängig vom Auto existieren.
# Wenn das Auto jedoch zerstört wird, können die Räder immer noch existieren.

# Komposition:
# Komposition ist eine stärkere Form der Aggregation.
# Hier ist das Teilobjekt vollständig im Besitz des ganzen Objekts, was bedeutet,
# dass es ohne das ganze Objekt nicht existieren kann.
# Wenn das ganze Objekt zerstört wird, werden auch seine Teilobjekte zerstört.
# Ein Beispiel für Komposition ist ein Computer und seine CPU.
# Die CPU ist ein wesentlicher Bestandteil des Computers,
# und ohne den Computer gibt es keine unabhängige Existenz der CPU.