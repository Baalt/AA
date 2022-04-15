from time import sleep
from bs4 import BeautifulSoup

from browser.head import Browser
from browser.buttons.referee import RefereeButtons
from scraper.referee import RefereeScraper


class RefereeManager(RefereeButtons):
    def __init__(self, browser: Browser, league: str, all_referee_data=dict):
        super().__init__(browser=browser)
        self.all_referee_data = all_referee_data()
        self.scraper = RefereeScraper()
        self.league = league

    @property
    def get_data(self):
        return self.all_referee_data

    def get_referee_data(self):
        self.open_referee_button.click()
        self.filter_out(number_of_matches=100)
        sleep(1)
        soup = BeautifulSoup(self.browser.get_html, 'lxml')
        self.scraper.scrap_referee_table(soup=soup,
                                         all_referee_data=self.all_referee_data)

        self.statistic_buttons[5].click()
        sleep(1)
        self.update_button.click()
        soup = BeautifulSoup(self.browser.get_html, 'lxml')
        self.scraper.scrap_referee_table(soup=soup,
                                         all_referee_data=self.all_referee_data)

    def filter_out(self, number_of_matches=100):
        self.quantity_of_matches_input, \
        self.quantity_of_matches_fix_input_clicker = self.quantity_of_matches_buttons

        self.quantity_of_matches_input.clear()
        self.quantity_of_matches_input.send_keys(number_of_matches)
        self.quantity_of_matches_fix_input_clicker.click()

        self.referee_season_button_all.click()
        self.current_league_buttons(league=self.league).click()
        self.update_button.click()
