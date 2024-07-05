# Handles entity actions
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Perform this action with the objects needed to determine its scope.

        'engine' is the scope this action is being performed in.

        'entity' is the object performing the action.

        Method must be overriden by Action subclass.
        """
        raise NotImplementedError()

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()

class MeleeAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return   # Did not find an entity to attack.
        
        print(f"You kick the {target.name}, much to its annoyance!")

# BumpAction Determines whether to call MovementAction or MeleeAction.
class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_x):
            # Moving into space blocked by entity -> MeleeAction
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            # Moving into space without blocking entity -> MovementAction
            return MovementAction(self.dx, self.dy).perform(engine, entity)

class MovementAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return   # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return   # Destination is blocked by tile.
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return   # Destination is blocked by an entity.
        
        entity.move(self.dx, self.dy)