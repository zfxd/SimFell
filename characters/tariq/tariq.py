"""Module for the Tariq Character."""

import random
from base import BaseCharacter

#TODO from spells import tariq spells
#TODO from talent import tariq talents

from .utils.enums import SpellSimFellName

# This is where you will define any custom features the character may have.
# Eg. Resources, References to Spells that all other spells can reference
# like Anima Spikes, and more.
class Tariq(BaseCharacter):
    """Defines the Tariq character class"""

    fury = 0

    # Ensure you pass down the args and kwargs and reset any default values.
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.fury = 0.0
        # Max fury scales off strength. Abilities cost %fury
        self.max_fury = self.main_stat * 12

        # NOTE: Consider doing the scaling on ability side instead, keeping fury clamped to the 0-100 range. Whether or not this is possible will depend on how the DifficultyScale actually changes in the fury formulas... In town, at least, it's been found to be a flat 1.0. Further data is required for behavior in dungeon.
        # TODO: Z - Verify this math with the data you have.

        # Fury formulas given below:
        # Ink.Rage.MaxRageMultiplier, 12; This is multiplied with his strength and will result in his total amount of max rage
        # Ink.Rage.RageIncreaseBaseline, 26; The rage will increase by (RageIncreaseBaseline) * (Damage done / (DifficultyDamageScale * 100)) to ensure that the rage increase is constant during levels
        # Ink.Rage.OutOfCombat.TickInterval, 1.0
        # Ink.Rage.OutOfCombat.AmountToSpendPerTick, 0.01 ; Percentage of Max Rage

    # add our list of spells the Hero can cast to the spells using the defined
    # simefell_name from the enums along with a new instance of the spell.
    def configure_spell_book(self):
        self.spells = []
        # TODO add spells

        # We then need to go through and add a reference to the character to
        # each spell. This is just for ease of access when casing the spells.
        for spell in self.spells.values():
            spell.character = self


    def add_talent(self, talent_identifier: str):
        # We need to get the talent from our list of talents.
        talent = TariqTalents.get_by_identifier(talent_identifier)
        # And then apply it to the list of talents.
        if talent is not None:
            self.talents.append(talent)
            # Note: If a talent were to provide a global passive to the hero.
            # EG. Rimes Avalanche giving 5% Crit Power, you would define/apply
            # That value to here.
            # if talent == RimeTalents.AVALANCHE:
            #     self.crit_power_multiplier += AvalancheTalent.bonus_crit_power
            # TODO Start thinking about how to handle Tariq's LIGHTNING ONLY crit damage?chance? increase...

    # TODO custom functions per hero go here.
    # Maybe rage handling functions...

    def gain_fury(self, amount):
        self.fury += amount
        if self.fury > self.max_fury:
            self.fury = self.max_fury
            # TODO possible overcap behavior / notification here

    def spend_fury(self, amount):
        if random.uniform(0, 100) < self.get_spirit():
            # TODO possible reporting of spirit reset here
            return

        self.fury -= amount
        if self.fury < 0:
            # TODO most likely an error. Might want to raise a warning here.
            self.fury = 0