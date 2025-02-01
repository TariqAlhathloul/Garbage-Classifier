import time
from LCD import LCD

def display_text(text: list, lines: list=[1, 2], sleep: int=7, I2C_address: int=0x27) -> None:
    """
    Display the text on the specified line of the LCD screen.
    :param text: The text to display.
    :param line: The line number on which to display the text.
    :param sleep: The duration to display the text.
    :param I2C_address: The I2C address of the LCD screen.
    :return: None
    """
    lcd = LCD(2, I2C_address, True)
    lcd.message(text[0], lines[0])
    lcd.message(text[1], lines[1])    
    time.sleep(sleep)
    lcd.clear()
  
if __name__ == "__main__":
    lines=[1, 2]
    text = ["Test", "Basket"]
    display_text(text, lines, 3)