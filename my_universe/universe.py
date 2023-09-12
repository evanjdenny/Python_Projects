"""Development of the different ways to view the sections of the universe."""
from enum import Enum

class ItemType(Enum):
    """Types of items."""
    GENERAL = 0
    MATERIAL = 1
    FURNITURE = 2
    BOOK = 3
    WEAPON = 4
    OFFHAND = 5
    CLOTHING = 6
    ARMOR = 7
    CURRENCY = 8
    JUNK = 9

class Uses(Enum):
    """Uses for Items."""
    NONE = 0
    GENERAL = 1
    EQUIP = 2
    READ = 3
    CAST = 4
    INTERACT = 5
    UNKNOWN = 6

class Item:
    """Item(s) """
    uses = None
    uses_general = {}
    uses_equip = {}
    uses_read = {}
    uses_cast = {}
    uses_interact = {}
    uses_unknown = {}
    uses_none = {}
    all_uses = [uses_general, uses_equip, uses_read, uses_cast, uses_interact, uses_unknown, uses_none]

    def __init__(self, name: str, description: str, item_type: ItemType, weight: float):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.weight = weight

    def __call__(self, target=None):
        self.use(target)

    def set_uses(self, uses: Uses):
        """Set Item.uses"""
        self.uses = uses

    def set_specific_use(self, use: int, key: str, value):
        self.all_uses[use][key] = value

    def __use(self, target='No Target'):
        if self.uses == Uses.GENERAL:
            self.uses_general.get(target)
        elif self.uses == Uses.EQUIP:
            self.uses_equip.get(target)
        elif self.uses == Uses.READ:
            self.uses_read.get(target)
        elif self.uses == Uses.CAST:
            self.uses_cast.get(target)
        elif self.uses == Uses.INTERACT:
            self.uses_interact.get(target)
        elif self.uses == Uses.UNKNOWN:
            self.uses_unknown.get(target)

    def use(self, target=None):
        if target is None:
            self.__use()
        else:
            self.__use(target)

class PlanetStats:
    """Statistics and Features of a Planet."""
    size: int | float # Measured in km
    habitable: bool # Habitable or Uninhabitable
    state_of_water: StateOfMatter # State of water on Planet's surface

class PlanetType(Enum):
    """Different types of Planets. Enumerations."""
    ROCKY_SMALL = 0 # MARS-LIKE
    ROCKY_MEDIUM = 1 # EARTH-LIKE
    ROCKY_LARGE = 2 # SUPER-EARTHS
    GAS_GIANT = 3 # NEPTUNE -> JUPITER
    MOON = 4 # MOONS

class Planet:
    """Planet orbiting a star."""
    def __init__(self, name: str, planet_type: None | PlanetType, planet_stats: None | PlanetStats):
        self.name = name
        self.planet_type = planet_type
        self.planet_stats = planet_stats

class Zone:
    """Zone with connecting Tiles."""
    tiles = tuple()
    description = str()

    def __init__(self, name: str, planet: Planet, parent_zone=None):
        self.name = name
        self.planet = planet
        self.parent_zone = parent_zone

class Tile:
    """The coordinate-based fundamental building block of any Zone. The 
    Tile is where the Player resides and can have anything from doors to
    walls, chests and lights, NPCs and monsters."""
    name: str # __init__ | Get/Set methods
    zone_parent = None # __init__
    zone_type = None # __init__
    contents = [] # Add/Remove/Clear methods
    beings = tuple() # Add/Remove methods
    size: int | float # __init__ | Get/Set methods
    connecting_tiles = tuple() # Connect/Disconnect methods
    zone_transition = False # Set method
    connecting_zone = None # Get/Set methods

    def __init__(self, name: str, zone, size: int | float):
        self.name = name
        self.zone = zone
        self.size = size

    def set_name(self, name):
        """Set Tile.name"""
        self.name = name

    def get_name(self): 
        """Return Tile.name"""
        return self.name

    def add_contents(self, content):
        """Add content(s) to Tile.contents"""
        if isinstance(content, list):
            for item in content:
                self.contents.append(item)
        else:
            self.contents.append(content)

    def delete_contents(self, content):
        """Remove content(s) from Tile.contents"""
        if isinstance(content, list):
            for item in content:
                self.contents.remove(item)
        else:
            self.contents.remove(content)

    def clear_contents(self):
        """Clear contents from Tile object"""
        self.contents.clear()

    def add_beings(self, being):
        """Add being(s) to Tile.beings"""
        if isinstance(being, tuple):
            for item in being:
                self.beings += item
        else:
            self.beings += being

    def remove_beings(self, being):
        """Remove being(s) from Tile.beings"""
        if isinstance(being, tuple):
            for item in being:
                self.beings += item
        else:
            self.beings += being

    def set_size(self, size: int | float):
        """Set the Tile.size value"""
        self.size = size

    def get_size(self):
        """Return Tile.size value"""
        return self.size

    def connect_tile(self, tile):
        """Connect Tile to this Tile instance"""
        self.connecting_tiles += tile

    def disconnect_tile(self, tile):
        """Disconnect Tile from this Tile instance"""
        self.connecting_tiles -= tile

    def set_zone_transition(self):
        """If Tile instance allows Player to transition to another Zone,
        set Tile.zone_transition to True. If Tile transition doesn't allow
        this, set Tile.zone_transition to False."""
        if self.zone_transition:
            self.zone_transition = False
        elif not self.zone_transition:
            self.zone_transition = True

    def set_connecting_zone(self, zone):
        """Set Tile.connecting_zone"""
        self.connecting_zone = zone

    def get_connecting_zone(self):
        """Return Tile.connecting_zone"""
        return self.connecting_zone

    def remove_connecting_zone(self):
        """Remove Tile.connecting_zone"""
        self.connecting_zone = None

class StateOfMatter(Enum):
    """States of matter."""
    UNKNOWN = 0
    LIQUID = 1
    SOLID = 2
    GAS = 3
    PLASMA = 4
