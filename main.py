# import os
# import subprocess
import random
from typing import List
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# original_directory = os.getcwd()

# try:
#     os.chdir(r"C:\Program Files\Google\Chrome\Application")

#     subprocess.run([
#         "chrome.exe",
#         "--remote-debugging-port=9222",
#         '--user-data-dir="C:\\selenium"'
#     ])

#     print("Chrome launched with remote debugging")

# finally:
#     os.chdir(original_directory)
#     print(f"Returned to the original directory: {original_directory}")

def __get_syllable(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    syllable_elements = soup.find_all(class_="syllable")

    if syllable_elements:
        return syllable_elements[0].get_text()
    return None

def __get_fitting_word(substring: str, words: List[str]) -> str | None:
    filtered_words = [word.strip() for word in words if substring in word]
    if filtered_words:
        word = random.choice(filtered_words)
        words.remove(f"{word}\n")
        return word
    return None

def __type_and_send_keys(wait, word: str):
    # typing_speed = random.randrange(7, 13)/100
    # typing_speed = 0.3 #15 ppm
    typing_speed = 0.1 #35 ppm
    typing_speed = 0.05 #48 ppm
    try:
        text_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selfTurn input[type='text']")))
        text_box.clear()
        for char in word:
            text_box.send_keys(char)
            sleep(typing_speed)
        text_box.send_keys(Keys.ENTER)
    except:
        pass

def __player_turn(driver):
    try:
        self_turn_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".selfTurn"))
        )
        if not self_turn_element.get_attribute("hidden"):
            return True
        else:
            return False
    except:
        return False

with open("br-sem-acentos.txt", 'r') as file:
    words = file.readlines()

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)

iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

# syllable_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "syllable")))

while True:
    if __player_turn(driver):
        substring = __get_syllable(driver)
        word = __get_fitting_word(substring, words)
        if word:
            __type_and_send_keys(wait, word)
            print(word)

    sleep(1)

