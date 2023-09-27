import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create(address="localhost", port=4711)

def execAufgabe(): 

    # Hole die aktuelle Position des Spielers
    player_pos = mc.player.getPos()

    block_materials = [1, 41, 57]

    for x_offset in range(3):
        for y_offset in range(4):
            for z_offset in range(5):
                # Berechne die Koordinaten für den aktuellen Block
                x = player_pos.x + x_offset
                y = player_pos.y + y_offset
                z = player_pos.z + z_offset

                # Wähle das Material für den aktuellen Block
                block_material = block_materials[(x_offset + y_offset + z_offset) % len(block_materials)]

                # Platziere den Block
 
    mc.postToChat("Blöcke platziert!")