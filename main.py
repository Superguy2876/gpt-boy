from pyboy import PyBoy, WindowEvent
import os
import sys
import io
import time
from key_handler import KeyHandler

from pyboy_ai.pkmnRed import PkmnRed



# get list of roms from roms folder
roms = os.listdir("roms")

print(roms)

rom_name = ""
# check if there are arguments and load the rom from the argument
if len(sys.argv) > 1 and sys.argv[1] in roms:
    rom_name = sys.argv[1]

# if no arguments are given, display menu
if len(sys.argv) == 1:
    print("Select a ROM to play:")
    for i, rom in enumerate(roms):
        print(f"{i}: {rom}")
    # get user input
    rom_index = int(input("Enter the number of the ROM you want to play: "))
    rom_name = roms[rom_index]

# print current working directory
print(os.getcwd())

# start emulator
pyboy = PyBoy("roms/" + rom_name, window_type="SDL2")
rBoy = PkmnRed(pyboy)
# set up window
keyboard = KeyHandler(list('1234'))
keyboard.start()

# main loop
while not pyboy.tick():
    # check for keyboard input
    if keyboard.is_pressed("1"):
        print("1 pressed")
        state_file = open("states/state1", "wb")
        pyboy.save_state(state_file)
        state_file.close()
    if keyboard.is_pressed("2"):
        print("2 pressed")
        state_file = open("states/state1", "rb")
        pyboy.load_state(state_file)
        state_file.close()
    if keyboard.is_pressed("3"):
        print("3 pressed")
        print(rBoy.get_pokemon_at(0))
    if keyboard.is_pressed("4"):
        print("4 pressed")
    pass