class Impossible(Exception):
    """
    Exception raised when an action is impossible to be performed.

    The reason is given as an exception message.
    ex: raise Impossible("Exception message")
    """

class QuitWithoutSaving(SystemExit):
    """
    Can be reaised to exit the game without automatically saving.
    """

