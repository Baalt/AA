from bs4 import BeautifulSoup


class MatchScheduleScraper:
    def scrap_football_matches_urls(self, soup):
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


class LeagueScraperMethods:
    def scrap_league_data(self, soup: BeautifulSoup):
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

    def scrap_statistic_name(self, soup: BeautifulSoup, tooltip=True):
        button_class = 'btn btn-sm btn-light active'
        if tooltip:
            button_class = button_class + ' has-tooltip'

        current_statistic_button_name = soup.find(
            'button', attrs={'class': button_class}
        ).get_text(strip=True)
        return current_statistic_button_name


class LeagueScraper(LeagueScraperMethods):
    def scraping(self, soup: BeautifulSoup, all_league_data: dict, tooltip=True):
        current_statistics_button_name = self.scrap_statistic_name(soup, tooltip=tooltip)
        league_data = self.scrap_league_data(soup)
        all_league_data[current_statistics_button_name] = league_data
        return all_league_data
