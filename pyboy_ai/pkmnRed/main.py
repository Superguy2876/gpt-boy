
from pyboy import PyBoy

POKEMON_PARTY_COUNT = 0xD163
POKEMON_PARTY_ID_START = 0xD164
POKEMON_PARTY_START = 0xD16B
POKEMON_STRUCT_SIZE = 44

POKEMON_INVENTORY_START = 0xD31D

POKEMON_OAK_EVENT = 0xD74E
POKEMON_POKEDEX_EVENT = 0xD74B


def _get_two_bytes(pyboy, address):
    return (pyboy.get_memory_value(address) <<
            8) + pyboy.get_memory_value(address + 0x1)


def _set_two_bytes(pyboy, address, value):
    pyboy.set_memory_value(address, value >> 8)
    pyboy.set_memory_value(address + 0x1, value & 0xFF)

class PkmnRed():

    _valid_states = ["Overworld", "Battle", "Menu", "Text", "Trade", "Evolution", "Cutscene"]

    def __init__(self, pyboy: PyBoy):
        self.redBoy = pyboy
        self.state = "Overworld"
    
    def get_party(self):
        return dict(map(lambda x: (x, self.get_pokemon(POKEMON_PARTY_START + x * POKEMON_STRUCT_SIZE)), range(POKEMON_PARTY_COUNT)))
    
    def get_pokemon_at(self, index: int):
        return self.get_pokemon(POKEMON_PARTY_START + index)

    def get_pokemon(self, offset):
        return {
            "id": self.redBoy.get_memory_value(offset),
            "hp": _get_two_bytes(self.redBoy, offset + 0x1),
            "level": self.redBoy.get_memory_value(offset + 0x21),
            "status": self.redBoy.get_memory_value(offset + 0x4),
            "type1": self.redBoy.get_memory_value(offset + 0x5),
            "type2": self.redBoy.get_memory_value(offset + 0x6),
            "move1": self.redBoy.get_memory_value(offset + 0x8),
            "move2": self.redBoy.get_memory_value(offset + 0x9),
            "move3": self.redBoy.get_memory_value(offset + 0xA),
            "move4": self.redBoy.get_memory_value(offset + 0xB),
            "max_hp": _get_two_bytes(self.redBoy, offset + 0x22),
            "attack": _get_two_bytes(self.redBoy, offset + 0x24),
            "defense": _get_two_bytes(self.redBoy, offset + 0x26),
            "speed": _get_two_bytes(self.redBoy, offset + 0x28),
            "special": _get_two_bytes(self.redBoy, offset + 0x2A)
        }

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        # check if state is valid
        if state in self._valid_states:
            self.state = state
        else:
            raise ValueError("Invalid state")
