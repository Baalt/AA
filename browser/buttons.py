from selenium.webdriver.common.by import By

from browser.head import Browser


class Button:
    def __init__(self, browser: Browser):
        self.browser = browser


class LeagueButtons(Button):
    @property
    def get_buttons(self):
        statistic_buttons_group = self.browser.firefox.find_element(By.XPATH,
                                                                    '//div[@class="btn-group stat-picker-desktop"]')
        statistic_buttons = statistic_buttons_group.find_elements(By.XPATH,
                                                                  '//button[@class="btn btn-sm btn-light has-tooltip"]')
        update_button = self.browser.firefox.find_element(By.XPATH,
                                                          '//button[@class="btn btn-sm btn-success w-100 my-1 mt-2"]')
        return statistic_buttons, update_button


class MatchButtons(Button):
    pass


if __name__ == '__main__':
    pass
