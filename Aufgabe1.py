import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create(address="localhost", port=4711)

def execAufgabe():  
    player_pos = mc.player.getPos()

    block_materials = [1, 41, 57]

    for x_offset in range(6):
        x = player_pos.x + x_offset
        mc.setBlock(x, player_pos.y, player_pos.z, block_materials[0])
    for y_offset in range(5):
        y = player_pos.y + y_offset
        mc.setBlock(x, y,player_pos.z, block_materials[1])
    for z_offset in range(4): 
        z = player_pos.z + z_offset
        mc.setBlock(x, player_pos.y, z, block_materials[2])
                

    mc.postToChat("Blöcke platziert!")

execAufgabe()
