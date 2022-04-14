from bs4 import BeautifulSoup

from scraper.parent import ScraperMethods


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
