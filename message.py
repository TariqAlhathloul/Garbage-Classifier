import time
from LCD import LCD

def display_text(text: str, line: int, sleep: int, I2C_address: int=0x27) -> None:
    """
    Display the text on the specified line of the LCD screen.
    :param text: The text to display.
    :param line: The line number on which to display the text.
    :param sleep: The duration to display the text.
    :param I2C_address: The I2C address of the LCD screen.
    :return: None
    """
    lcd = LCD(2, I2C_address, True)
    lcd.message(text, line)        
    time.sleep(sleep)
    lcd.clear()
  
if __name__ == "__main__":
    pass