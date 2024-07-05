from entity import Entity

# The user-controlled player entity
player = Entity(
    char = "@", 
    color = (255, 255, 255), 
    name = "Player", 
    blocks_movement = True
    )

# Weaker enemy, high chance of spawning
orc = Entity(
    char = "o", 
    color = (63, 127, 63), 
    name = "Orc", 
    blocks_movement = True
    )

# Stronger enemy, low chance of spawning
troll = Entity(
    char = "T",
    color = (0, 127, 0),
    name = "Troll",
    blocks_movement = True
)