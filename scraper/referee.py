from bs4 import BeautifulSoup

from scraper.parent import ScraperMethods
from kernel.filters.convert_from_big_data_to_math_input import MatchDataNormalize


class RefereeScraper(ScraperMethods):
    def scrap_referee_table(self, soup: BeautifulSoup, all_referee_data: dict):
        statistic_name = self.scrap_statistic_name(soup=soup)
        all_referee_data[statistic_name] = []
        table = soup.find('table',
                          id='table').find('tbody').find_all('tr',
                                                             attrs={'class': "match-row"})
        for row in table:
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

            all_referee_data[statistic_name].append(data_collect)
