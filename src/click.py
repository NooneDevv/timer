import time
import threading
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key
from pynput.keyboard import Controller as control
keyboard = control()
button = Button.left
start_stop_key = KeyCode(char='q')
exit_key = KeyCode(char='w')


class ClickMouse(threading.Thread):
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            i = 0
            while self.running:
                if i > 20:
                    keyboard.touch(Key.esc,True)
                    mouse.click(self.button)
                    keyboard.touch(Key.esc,True)
                    i=random.randint(0,6)
                mouse.click(self.button)
                time.sleep(random.uniform(0.2,0.6))
                i+=1



mouse = Controller()
click_thread = ClickMouse(button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.stop_clicking()



with Listener(on_press=on_press) as listener:
    listener.join()