from time import sleep
from bs4 import BeautifulSoup

from browser.head import Browser
from browser.buttons.league import LeagueButtons
from scrapers.league import LeagueScraper


class LeagueManager(LeagueButtons):
    def __init__(self, browser: Browser, soup: BeautifulSoup):
        super().__init__(browser)
        self.browser: Browser = browser
        self.soup: BeautifulSoup = soup
        self.league_scraper = LeagueScraper()

    @property
    def get_data(self):
        all_league_data: dict = {}
        self.league_scraper.scrap(self.soup, all_league_data, tooltip=True, goal=True)
        for button in self.statistic_buttons[1:10]:
            button.click()
            sleep(1)

            self.update_button.click()
            sleep(1)

            self.soup = BeautifulSoup(self.browser.get_html, 'lxml')
            self.league_scraper.scrap(self.soup, all_league_data)

        return all_league_data
