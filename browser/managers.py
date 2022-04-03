from pprint import pprint
from time import sleep

from bs4 import BeautifulSoup

from browser.buttons import LeagueButtons
from browser.buttons import Browser
from scraper.directions import LeagueScraper




class LeagueManager:
    def __init__(self, browser: Browser, soup: BeautifulSoup):
        self.browser = browser
        self.soup = soup
        self.statistic_buttons, self.update_button = LeagueButtons(self.browser).get_buttons
        self.league_scraper = LeagueScraper()

    def get_league_data(self):
        all_league_data = {}
        self.league_scraper.scraping(self.soup, all_league_data)
        for button in self.statistic_buttons:
            button.click()
            self.update_button.click()
            self.soup = BeautifulSoup(self.browser.get_html, 'lxml')
            sleep(1)
            self.league_scraper.scraping(self.soup, all_league_data, tooltip=False)
            sleep(1)
        pprint(all_league_data)
