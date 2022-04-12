from bs4 import BeautifulSoup
from scraper.sort import MatchDataNormalize


class MatchScheduleScraper:
    def scrap_shedule_data(self, soup: BeautifulSoup) -> dict:
        schedule = {}
        league_name = None
        table_rows = soup.find('table').find_all('tr')
        for row in table_rows:
            try:
                league_name = row.find('a', attrs={'class': 'league-link'}).get_text(strip=True)
                league_url = row.find('a', attrs={'class': 'league-link'})['href']
                schedule[league_name] = {'league_url': league_url, 'match_url': []}

            except (AttributeError, TypeError):
                pass

            try:
                match_url = \
                    row.find('td', attrs={'class': 'text-right align-middle upcoming-match-prematch'}).find('a')['href']
                schedule[league_name]['match_url'].append(match_url)

            except (AttributeError, TypeError):
                pass

        return schedule


class ScraperMethods:
    def scrap_statistic_name(self, soup: BeautifulSoup, tooltip=False) -> str:
        button_class = 'btn btn-sm btn-light active'
        if tooltip:
            button_class = button_class + ' has-tooltip'

        current_statistic_button_name = soup.find(
            'button', attrs={'class': button_class}
        ).get_text(strip=True)

        return current_statistic_button_name


class LeagueScraper(ScraperMethods):
    def scrap_league_data(self, soup: BeautifulSoup) -> dict:
        league_data = {}
        table_rows = soup.find('table').find_all('tr')
        for row in table_rows:
            try:
                row_data = row.find_all('td')
                position = row_data[0].get_text()
                command = row_data[1].get_text()
                games_count = row_data[2].get_text()
                league_data[command] = {'position': position, 'games_count': games_count}

            except IndexError:
                pass

        return league_data

    def scrap(self, soup: BeautifulSoup, all_league_data: dict, tooltip=False) -> dict:
        current_statistics_button_name = self.scrap_statistic_name(soup, tooltip=tooltip)
        league_data = self.scrap_league_data(soup)
        all_league_data[current_statistics_button_name] = league_data

        return all_league_data


class MatchScraper(ScraperMethods):
    def __init__(self, soup: BeautifulSoup, all_match_data: dict):
        self.soup = soup
        self.all_match_data: dict = all_match_data

    def __str__(self) -> str:
        return '{}'.format(self.all_match_data)

    def show_data(self):
        print(self.all_match_data)

    def scrap_commands_name(self):
        self.home_command_name = self.soup.find_all('div',
                                                    attrs={'class': "media-body"})[0].find('a').get_text(strip=True)
        self.away_command_name = self.soup.find_all('div',
                                                    attrs={'class': "media-body"})[1].find('a').get_text(strip=True)

        self.all_match_data['home_command_name'] = self.home_command_name
        self.all_match_data['away_command_name'] = self.away_command_name

    def scrap_match_table_data(self, soup):
        home_table = soup.find_all('table',
                                   id='table')[0].find('tbody').find_all('tr',
                                                                         attrs={'class': "match-row"})
        away_table = soup.find_all('table',
                                   id='table')[1].find('tbody').find_all('tr',
                                                                         attrs={'class': "match-row"})

        self.statistic_name = self.scrap_statistic_name(soup=soup)
        self.all_match_data[self.statistic_name] = {'home_collections': list(), 'away_collections': list()}

        [self.scrap_them_collect_to_global_storage(row, 'home_collections') for row in home_table if len(row) > 5]
        [self.scrap_them_collect_to_global_storage(row, 'away_collections') for row in away_table if len(row) > 5]

    def scrap_them_collect_to_global_storage(self, row: BeautifulSoup, key: str):
        season = row.find_all('td')[1].find('a').get_text(strip=True)
        day_month = row.find_all('td')[2].get_text(strip=True)

        dmY = MatchDataNormalize(season=season, day_month=day_month).convert_season_to_dmY()

        home_command = row.find_all('td')[3].find('a').get_text(strip=True)
        away_command = row.find_all('td')[6].find('a').get_text(strip=True)

        home_command_individual_total = row.find_all('td')[4].get_text(strip=True)
        away_command_individual_total = row.find_all('td')[5].get_text(strip=True)

        data_collect = [dmY,
                        home_command,
                        away_command,
                        home_command_individual_total,
                        away_command_individual_total]

        self.all_match_data[self.statistic_name][key].append(data_collect)


    def scrap_coefficients_total(self, soup: BeautifulSoup):
        pass

