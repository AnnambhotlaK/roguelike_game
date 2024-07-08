from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

# The user-controlled player entity
player = Actor(
    char = "@", 
    color = (255, 255, 255), 
    name = "Player", 
    ai_cls = HostileEnemy,
    fighter = Fighter(hp = 30, defense = 2, power = 5)
    )

# Weaker enemy, high chance of spawning
orc = Actor(
    char = "o", 
    color = (63, 127, 63), 
    name = "Orc", 
    ai_cls = HostileEnemy,
    fighter = Fighter(hp = 10, defense = 0, power = 3)
    )

# Stronger enemy, low chance of spawning
troll = Actor(
    char = "T",
    color = (0, 127, 0),
    name = "Troll",
    ai_cls = HostileEnemy,
    fighter = Fighter(hp = 16, defense = 1, power = 4),
)