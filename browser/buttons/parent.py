from selenium.webdriver.common.by import By

from browser.head import Browser


class Button:
    def __init__(self, browser: Browser):
        self.browser = browser

    @property
    def update_button(self):
        UPDATE_BUTTON_XPATH = '//button[@class="btn btn-sm btn-success w-100 my-1 mt-2"]'
        update_button = self.browser.firefox.find_element(By.XPATH,
                                                          value=UPDATE_BUTTON_XPATH)

        return update_button

    @property
    def statistic_buttons(self):
        STATISTIC_BUTTONS_XPATH = '//div[contains(@class, "stat-picker-desktop")]' \
                                  '/button[contains(@class, "btn btn-sm btn-light")]'
        statistic_buttons = self.browser.firefox.find_elements(By.XPATH,
                                                               value=STATISTIC_BUTTONS_XPATH)

        return statistic_buttons