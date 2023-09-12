class Spell:
    def __init__(self, name, description, type_of_magick, effect, damage, dot, damage_type):
        self.name = name
        self.description = description
        self.type_of_magick = type_of_magick
        self.effect = effect
        self.damage = damage
        self.dot = dot
        self.damage_type = damage_type

    def __call__(self, primary_target=None, secondary_target=None):
        self.effect(primary_target, secondary_target)

spell_push_1 = Spell('Push', 'Pushes an Item or Being from one Tile to a Tile further away from you.', 'Force', 'TBD', 0.0, 0.0, None)

class BookOfSpellsVolumeOne:
    spells = ['Push', 'Pull', 'Ignite', '']
