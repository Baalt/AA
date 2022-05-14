from selenium import webdriver
from selenium.webdriver.common.by import By

from config import SOURCE, LOGIN, PASSWORD


class Browser:
    def __init__(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()

    @property
    def get_html(self):
        return self.firefox.page_source

    def open_new_page(self, match_url: str):
        match_url = SOURCE + match_url
        self.firefox.get(match_url)

    def login(self):
        self.firefox.get(SOURCE + '/login')
        self.firefox.implicitly_wait(10)

        email = self.firefox.find_element(By.ID, 'email', )
        password = self.firefox.find_element(By.ID, 'password')

        email.send_keys(LOGIN)
        password.send_keys(PASSWORD)
        self.firefox.implicitly_wait(10)

        ENTER_BUTTON_XPATH =  "//button[text()='Войти']"
        self.firefox.find_element(By.XPATH, ENTER_BUTTON_XPATH).click()

    def close(self):
        self.firefox.close()