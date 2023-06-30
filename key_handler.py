import pynput

class KeyHandler:
    def __init__(self, keys: list) -> None:
        self.keys = {key: {'pressed': False, 'processed': False} for key in keys}
        self.listener = pynput.keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def on_press(self, key):
        try:
            key_str = key.char
        except AttributeError:
            key_str = str(key)

        if key_str in self.keys and not self.keys[key_str]['pressed']:
            self.keys[key_str]['pressed'] = True
            self.keys[key_str]['processed'] = False
    
    def on_release(self, key):
        try:
            key_str = key.char
        except AttributeError:
            key_str = str(key)

        if key_str in self.keys:
            self.keys[key_str]['pressed'] = False
            self.keys[key_str]['processed'] = False

    def is_pressed(self, key):
        if key in self.keys and self.keys[key]['pressed'] and not self.keys[key]['processed']:
            self.keys[key]['processed'] = True
            return True
        return False
    
    def stop(self):
        self.listener.stop()
        self.listener.join()

    def start(self):
        self.listener.start()
