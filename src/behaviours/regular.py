from time import sleep
from selenium.webdriver.remote.webdriver import WebElement
from src.behaviours import behaviour

class Regular(behaviour):

    def execute(text_box: WebElement, word: str):
        for char in word:
            text_box.send_keys(char)
            sleep(typing_speed)