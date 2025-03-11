"""Module for Tariq Buffs"""

from base import BaseBuff

class TariqBuff(BaseBuff):
    """Base class for all Tariq buffs."""

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        # As always pass up the base.
        super().__init__(*args, **kwargs)

        # TODO: Verify if Tariq buffs have any shared behavior.
        # Off the top of my head, that's a no.
        # Focused Wrath, Spirit buff, Thunder Call. 

    # Note: You can define more overrides here if you wish. BaseBuffs come
    # from the BaseSpell class so all overrides are still valid here.
