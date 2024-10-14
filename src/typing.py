import random
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Typing:
    def __init__(self, wait: WebDriverWait) -> None:
        self.wait = wait

    def type_word():
        pass

    def __regular_type(self, word):
        # typing_speed = random.randrange(7, 13)/100
        try:
            text_box = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selfTurn input[type='text']")))
            text_box.clear()
            # for char in word:
                # text_box.send_keys(char)
                # sleep(typing_speed)
            text_box.send_keys(Keys.ENTER)
        except:
            pass