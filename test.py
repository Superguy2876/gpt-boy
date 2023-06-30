from key_handler import KeyHandler

keyboard = KeyHandler(list('1234'))
keyboard.start()

while True:
    if keyboard.is_pressed("1"):
        print("1 pressed")
    if keyboard.is_pressed("2"):
        print("2 pressed")
    if keyboard.is_pressed("3"):
        print("3 pressed")
    if keyboard.is_pressed("4"):
        print("4 pressed")
    pass