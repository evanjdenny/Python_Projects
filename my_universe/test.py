"""Testing world-building using custom classes from modules in directory and subdirectories."""
from universe import Planet, PlanetStats, PlanetType, Zone, Tile, Item, ItemType, Uses

terra_stats = PlanetStats()
terra = Planet('Terra', PlanetType.ROCKY_MEDIUM, terra_stats)
metropolis = Zone('Metropolis', terra)
metropolis_atola_correctional_center = Zone('Atola Correctional Center', terra, metropolis)
metropolis_tile0_cell = Tile('Cell', metropolis_atola_correctional_center, 30.0)
book_of_spells_vol_1 = Item('Book of Spells: Volume 1', "A book containing novice level spells of many unsanctioned and illegal forms of MAGICK.", ItemType.BOOK, 0.0)
book_of_spells_vol_1.set_specific_use(2, 'No Target', )