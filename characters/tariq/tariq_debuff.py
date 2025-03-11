"""Module for Tariq Debuffs"""

from base import BaseDebuff

class Tariq(BaseDebuff):
    """Base class for all Tariq debuffs."""

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        # As always pass up the base.
        super().__init__(*args, **kwargs)

    # Note: You can define more overrides here if you wish. BaseDebuff come
    # from the BaseSpell class so all overrides are still valid here.
