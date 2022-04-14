from bs4 import BeautifulSoup

from scraper.parent import ScraperMethods
from scraper.sort import MatchDataNormalize


class MatchScraper(ScraperMethods):
    def __init__(self, all_match_data: dict):
        self.all_match_data: dict = all_match_data

    def __str__(self) -> str:
        return '{}'.format(self.all_match_data)

    def show_data(self):
        print(self.all_match_data)

    def scrap_commands_name(self, soup: BeautifulSoup):
        self.home_command_name = soup.find_all('div',
                                               attrs={'class': "media-body"})[0].find('a').get_text(strip=True)
        self.away_command_name = soup.find_all('div',
                                               attrs={'class': "media-body"})[1].find('a').get_text(strip=True)

        self.all_match_data['home_command_name'] = self.home_command_name
        self.all_match_data['away_command_name'] = self.away_command_name

    def scrap_match_table_data(self, soup, tooltip=False):
        home_table = soup.find_all('table',
                                   id='table')[0].find('tbody').find_all('tr',
                                                                         attrs={'class': "match-row"})
        away_table = soup.find_all('table',
                                   id='table')[1].find('tbody').find_all('tr',
                                                                         attrs={'class': "match-row"})

        self.statistic_name = self.scrap_statistic_name(soup=soup, tooltip=tooltip)
        self.all_match_data[self.statistic_name] = {'home_collections': list(), 'away_collections': list()}

        [self.scrap_them_collect_to_global_storage(row, 'home_collections') for row in home_table if len(row) > 5]
        [self.scrap_them_collect_to_global_storage(row, 'away_collections') for row in away_table if len(row) > 5]

    def scrap_them_collect_to_global_storage(self, row: BeautifulSoup, home_away_key: str):
        season = row.find_all('td')[1].find('a').get_text(strip=True)
        day_month = row.find_all('td')[2].get_text(strip=True)

        dmY = MatchDataNormalize(season=season, day_month=day_month).convert_season_to_dmY()

        home_command = row.find_all('td')[3].find('a').get_text(strip=True)
        away_command = row.find_all('td')[6].find('a').get_text(strip=True)

        home_command_individual_total = row.find_all('td')[4].get_text(strip=True)
        away_command_individual_total = row.find_all('td')[5].get_text(strip=True)

        data_collect = {'dmY': dmY,
                        'home_command': home_command,
                        'away_command': away_command,
                        'home_command_individual_total': home_command_individual_total,
                        'away_command_individual_total': away_command_individual_total}

        self.all_match_data[self.statistic_name][home_away_key].append(data_collect)