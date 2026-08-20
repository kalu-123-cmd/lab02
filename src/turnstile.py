"""Class under test for Lab 2, part three.

A turnstile with two states, used for state transition testing. Events
that are not valid in the current state are ignored, leaving the state
unchanged.
"""


class Turnstile:
    """A two state turnstile: ``"locked"`` or ``"unlocked"``.

    Valid transitions:
        locked   + coin  -> unlocked
        unlocked + push  -> locked

    Ignored events (state unchanged):
        locked   + push
        unlocked + coin
    """

    def __init__(self) -> None:
        self.state = "locked"

    def coin(self) -> None:
        """Insert a coin. Unlocks the turnstile only when it is locked."""
        if self.state == "locked":
            self.state = "unlocked"

    def push(self) -> None:
        """Push the arm. Locks the turnstile only when it is unlocked."""
        if self.state == "unlocked":
            self.state = "locked"
