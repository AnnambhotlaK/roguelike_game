# Runs the game

#!/usr/bin/env python3
import traceback

import tcod

import color
import exceptions
import input_handlers
import setup_game


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """
    If the current event handler has an active Engine,
    then save it.
    """
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")

def toggle_fullscreen(context: tcod.context.Context) -> None:
    """Toggle a context window between fullscreen and windowed modes."""
    window = context.sdl_window
    if not window:
        return
    if window.fullscreen:
        window.fullscreen = False
    else:
        window.fullscreen = tcod.sdl.video.WindowFlags.FULLSCREEN_DESKTOP

def main() -> None:

    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "8x8sprites.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new(
        x=None,
        y=None,
        width=screen_width,
        height=screen_height,
        columns=None,
        rows=None,
        renderer=None,
        tileset=tileset,
        vsync=True,
        sdl_window_flags=tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP,
        title="Untitled Roguelike",
    ) as context:

        root_console = tcod.console.Console(screen_width, screen_height, order="F")

        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle excpetions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


# Runs main when explicitly running the script
if __name__ == "__main__":
    main()
