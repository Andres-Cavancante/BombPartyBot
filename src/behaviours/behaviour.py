from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebElement

class behaviour(ABC):
    def __init__(self, typing_speed) -> None:
        self.typing_speed = typing_speed

    @abstractmethod
    def execute(text_box: WebElement, word: str) -> None:
        pass