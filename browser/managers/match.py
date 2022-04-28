from time import sleep
from bs4 import BeautifulSoup

from browser.head import Browser
from browser.buttons.match import MatchButtons
from scraper.match import MatchScraper


class MatchManager(MatchButtons):
    def __init__(self, browser: Browser, league: str, all_match_data=dict):
        super().__init__(browser)
        self.browser: Browser = browser
        self.league = league
        self.all_match_data = all_match_data()

        self.match_scraper = MatchScraper(all_match_data=self.all_match_data)
        # buttons
        self.quantity_of_matches_input, \
        self.quantity_of_matches_fix_input_clicker = self.quantity_of_matches_buttons

        self.season_home_button_all, \
        self.season_away_button_all = self.teams_season_buttons_all

        self.current_league_home_command_button, \
        self.current_league_away_command_button = self.current_league_command_buttons(league=self.league)

    @property
    def get_data(self):
        return self.all_match_data

    def filter_out(self, number_of_matches: int = 100):
        self.quantity_of_matches_input.clear()
        self.quantity_of_matches_input.send_keys(number_of_matches)
        self.quantity_of_matches_fix_input_clicker.click()
        sleep(1)

        self.season_home_button_all.click()
        self.season_away_button_all.click()

        self.current_league_home_command_button.click()
        self.current_league_away_command_button.click()
        sleep(1)

        self.update_button.click()

    def get_match_data(self, soup: BeautifulSoup):
        self.match_scraper.scrap_commands_name(soup=soup)
        try:
            self.match_scraper.get_count_of_games_and_name_with_last_trainer(soup=soup)
            self.match_scraper.scrap_match_table_data(soup=soup)

            for button in self.statistic_buttons[1:10]:
                button.click()
                sleep(1)

                self.update_button.click()
                sleep(1)

                new_soup = BeautifulSoup(self.browser.get_html, 'lxml')
                self.match_scraper.scrap_match_table_data(soup=new_soup)

            return True

        except IndexError:
            return None
