from time import sleep
from bs4 import BeautifulSoup

from browser.buttons import LeagueButtons, MatchButtons
from browser.buttons import Browser
from scraper.directions import LeagueScraper, MatchScraper, CoefficientScraper, ScraperMethods


class LeagueManager(LeagueButtons):
    def __init__(self, browser: Browser, soup: BeautifulSoup):
        super().__init__(browser)
        self.browser: Browser = browser
        self.soup: BeautifulSoup = soup
        self.league_scraper = LeagueScraper()

    def get_data(self):
        all_league_data: dict = {}
        self.league_scraper.scrap(self.soup, all_league_data, tooltip=True)
        for button in self.statistic_buttons[1:10]:
            button.click()
            sleep(1)

            self.update_button.click()
            sleep(1)

            self.soup = BeautifulSoup(self.browser.get_html, 'lxml')
            self.league_scraper.scrap(self.soup, all_league_data)

        return all_league_data


class MatchManager(MatchButtons):
    def __init__(self, browser: Browser, league: str, all_match_data=dict):
        super().__init__(browser)
        self.browser: Browser = browser
        self.league = league
        self.all_match_data = all_match_data()

        self.match_scraper = MatchScraper(all_match_data=self.all_match_data)
        # buttons
        self.quantity_of_matches_input, \
        self.quantity_of_matches_fix_input_clicker = self.quantity_of_matches_button

        self.season_home_button_all, \
        self.season_away_button_all = self.teams_season_buttons_all

        self.current_league_home_command_button, \
        self.current_league_away_command_button = self.current_league_command_buttons(league=self.league)

    @property
    def match_data(self):
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
        self.match_scraper.scrap_match_table_data(soup=soup)

        for button in self.statistic_buttons[1:10]:
            button.click()
            sleep(1)

            self.update_button.click()
            sleep(1)

            new_soup = BeautifulSoup(self.browser.get_html, 'lxml')
            self.match_scraper.scrap_match_table_data(soup=new_soup)


class CoefficientManager(MatchButtons, ScraperMethods):
    def __init__(self, browser: Browser, all_coefficient_data=dict):
        super().__init__(browser)
        self.all_coefficient_data = all_coefficient_data()
        self.coefficient_scraper = CoefficientScraper()

    @property
    def coefficient_data(self):
        return self.all_coefficient_data

    def create_dict_structure(self, soup: BeautifulSoup, tooltip=False):
        self.all_coefficient_data[self.scrap_statistic_name(soup=soup, tooltip=tooltip)] = {
            'total&coefficient': [],
            'total_1_&coefficient': [],
            'total_2_&coefficient': [],
            'handicap_1_&coefficient': [],
            'handicap_2_&coefficient': [],
        }

    def get_coefficients_data(self):
        self.coefficient_button.click()
        sleep(6)  # find element location By.XPATH or del slep and try scrap data

        soup = BeautifulSoup(self.browser.get_html, 'lxml')
        self.create_dict_structure(soup=soup, tooltip=True)
        self.coefficient_scraper.get_totals_data(soup=soup,
                                                 all_coefficient_data=self.all_coefficient_data,
                                                 tooltip=True)

        for button in self.statistic_buttons[1:10]:
            button.click()
            sleep(1)

            self.update_button.click()
            sleep(1)

            soup = BeautifulSoup(self.browser.get_html, 'lxml')
            self.create_dict_structure(soup=soup)
            self.coefficient_scraper.get_totals_data(soup=soup,
                                                     all_coefficient_data=self.all_coefficient_data,
                                                     tooltip=False)

        self.coefficient_handicap_button.click()

        for button in self.statistic_buttons[0:10]:
            button.click()

            self.update_button.click()
            sleep(1)

            soup = BeautifulSoup(self.browser.get_html, 'lxml')
            self.coefficient_scraper.get_handicap_data(soup=soup,
                                                       all_coefficient_data=self.all_coefficient_data,
                                                       tooltip=False)
