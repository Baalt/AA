from time import sleep
from bs4 import BeautifulSoup

from browser.head import Browser
from browser.buttons.match import MatchButtons
from scrapers.parent import ScraperMethods
from scrapers.coefficients import CoefficientsScraper


class CoefficientManager(MatchButtons, ScraperMethods):
    def __init__(self, browser: Browser, all_coefficient_data=dict):
        super().__init__(browser)
        self.all_coefficient_data = all_coefficient_data()
        self.coefficient_scraper = CoefficientsScraper()

    @property
    def get_data(self):
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
        self.open_coefficient_button.click()
        sleep(6)  # find element location By.XPATH

        # try:
        #     XPATH = '//div[@class="card-body"]'
        #     myElem = WebDriverWait(self.browser.firefox, 20).until(EC.presence_of_element_located((By.XPATH, XPATH)))
        #
        # except TimeoutException:
        #     pass

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
