from selenium import webdriver
from selenium.webdriver.common.by import By

from config import LOGIN, PASSWORD

class Browser :
    def __init__(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get('https://smart-tables.ru/login')
        self.firefox.implicitly_wait(10)

        email = self.firefox.find_element(By.ID, 'email', )
        password = self.firefox.find_element(By.ID, 'password')

        email.send_keys(LOGIN)
        password.send_keys(PASSWORD)
        self.firefox.implicitly_wait(10)

        self.firefox.find_element(By.XPATH, "//button[text()='Войти']").click()

    @property
    def get_html(self):
        return self.firefox.page_source

    def open_new_page(self, match_url: str):
        match_url = 'https://smart-tables.ru' + match_url
        self.firefox.get(match_url)
