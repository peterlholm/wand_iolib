from sys import path
path.append("/usr/local/lib/wand/iolib")
from ioLib2 import WandIO
import time
from typing import Callable, Optional
import gpiod

class Button:
    def __init__(self):
        """
        Initializes the Button class with a WandIO instance.
        """



    def set_button_interrupt(self, callback = None, longPress_callback = None, hold_time = None, button = None) -> None:
        """
        Sets up an interrupt for the specified button.

        Args:
            callback (Callable[[gpiod.LineEvent], None]): The callback function to handle the interrupt.
            longPress_callback (Callable): Callback function to handle long press.
            hold_time (float): time until hold func is envoked
            button (str): The button identifier ("front_top", "front_button", or "onoff_button").
        """


    def release_button(self, button: str = None) -> None:
        """
        Releases the specified button or all button if unspecified

        Args:
            button (str): The button to release, if not specified all buttons are released.
        """


    def reset_button(self) -> None:
        """
        Resets the button by toggling its output state.
        """



    def set_on_off_button_interrupt(self, callback: Callable[[gpiod.LineEvent], None]) -> None:
        """
        Sets up an interrupt for the on/off button press.

        Args:
            callback (Callable[[gpiod.LineEvent], None]): The callback function to handle the interrupt.
        """


if __name__ == "__main__":
    import time

    def int_callback(event: gpiod.LineEvent) -> None:
        print("interrupt")

    def onoff_callback(event: gpiod.LineEvent) -> None:
        print("interrupt_onoff")

    def hold():
        print("holding123")

    button = Button()
    #button.set_button_interrupt(callback=int_callback, button="front_button1")
    button.set_button_interrupt(callback=int_callback, button="front_button1")
    button.set_button_interrupt(callback=int_callback, longPress_callback=hold, hold_time = 0.5, button="front_button2")
    button.set_button_interrupt(callback=onoff_callback,longPress_callback=hold, hold_time = 2, button="onoff_button")
    # button.wand.set_output("mcp", 1, 1)

    while True:
        reset = input("press enter to reset")
        button.reset_button()
        #wand = WandIO()
        #print(wand.read_input("mcp", 2))
        time.sleep(0.1)
