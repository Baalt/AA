from bs4 import BeautifulSoup

from scrapers.parent import ScraperMethods


class LeagueScraper(ScraperMethods):
    def scrap_league_data(self, soup: BeautifulSoup, goal=False) -> dict:
        league_data = {}
        table_rows = soup.find('table').find_all('tr')
        for row in table_rows:
            try:
                row_data = row.find_all('td')
                position = row_data[0].get_text()
                command = row_data[1].get_text()
                games_count = row_data[2].get_text()
                try:
                    if goal:
                        average_total = row_data[11].get_text()
                        individual_total = row_data[12].get_text()
                        opposing_total = row_data[13].get_text()
                        points = row_data[8].get_text()
                        league_data[command] = {'position': position, 'games_count': games_count, 'points': points,
                                                'total': '{} | {} | {}'.format(average_total, individual_total,
                                                                               opposing_total)}
                    else:
                        average_total = row_data[9].get_text()
                        individual_total = row_data[6].get_text()
                        opposing_total = row_data[7].get_text()
                        league_data[command] = {'position': position, 'games_count': games_count,
                                                'total': '{} | {} | {}'.format(average_total, individual_total, opposing_total)}
                except KeyError as err:
                    print(err)
                    raise err

            except IndexError:
                pass

        return league_data

    def scrap(self, soup: BeautifulSoup, all_league_data: dict, tooltip=False, goal=False) -> dict:
        current_statistics_button_name = self.scrap_statistic_name(soup, tooltip=tooltip)
        league_data = self.scrap_league_data(soup, goal=goal)
        all_league_data[current_statistics_button_name] = league_data

        return all_league_data
