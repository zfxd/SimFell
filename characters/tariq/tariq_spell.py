"""Module for Tariq's spells."""

from base import BaseSpell

# Defines a template hero spell from the BaseSpell class. The reason for the
# per hero spell is due to not all heroes sharing a similar resource.
# EG: Rime uses Winter Orbs and Anima, and Ardeos uses Embers.
class TariqSpell(BaseSpell):
    """Defines a Tariq spell"""

    # Here is where you would define any additional features the hero spell
    # Might use, for Tariq, a fury cost, in %fury
    fury_cost = 0

    def __init__(
        self,
        *args,
        fury_cost=0,
        **kwargs,
    ):
        # Ensure you always pass down the arguments.
        super().__init__(*args, **kwargs)

        self.fury_cost = fury_cost

    # Override the is_ready function to ensure we have enough rage to
    # cast a spell, along with the base is_ready
    def is_ready(self):
        return (
            super().is_ready() # Base, and
            and (self.character.fury / self.character.max_fury) >= self.fury_cost
        )

    def fury_gained(self, damage=0):
        """Calculates the fury gained by the spell"""
        # Tariq spells can gain fury in various ways.
        # Leap Smash gives a flat 25%. Spenders don't gain fury.
        # The rest scale off damage done.
        return 0.0

    # Override the on_cast_complete to add spending behavior
    def on_cast_complete(self):
        super().on_cast_complete() # Once again, ensure you call the base.
        if self.fury_cost > 0:
            self.character.spend_fury(self.fury_cost)