from bs4 import BeautifulSoup

from scraper.parent import ScraperMethods


class CoefficientsScraper(ScraperMethods):
    def get_totals_data(self, soup: BeautifulSoup, all_coefficient_data: dict, tooltip=False):
        data = soup.find_all('table',
                             attrs={'class': "table-sm table table-bordered matches betting-table text-center"})

        for row in data:
            row = row.get_text().split('%')

            for each_data in row:
                coefficient_data_row_list = each_data.split()
                if len(coefficient_data_row_list) == 9:
                    total_number = coefficient_data_row_list[5]
                    coefficient_over = coefficient_data_row_list[-3]
                    coefficient_under = coefficient_data_row_list[-2]

                    all_coefficient_data[self.scrap_statistic_name(soup=soup, tooltip=tooltip)][
                        'total&coefficient'].append(
                        {'total_number': total_number,
                         'coefficient_under': coefficient_under,
                         'coefficient_over': coefficient_over})

                elif len(coefficient_data_row_list) == 11:
                    home_or_away_number = coefficient_data_row_list[2]
                    total_number = coefficient_data_row_list[-4]
                    coefficient_over = coefficient_data_row_list[-3]
                    coefficient_under = coefficient_data_row_list[-2]

                    all_coefficient_data[self.scrap_statistic_name(soup=soup, tooltip=tooltip)][
                        f'total_{home_or_away_number}_&coefficient'].append(
                        {'total_number': total_number,
                         'coefficient_under': coefficient_under,
                         'coefficient_over': coefficient_over})

    def get_handicap_data(self, soup: BeautifulSoup, all_coefficient_data: dict, tooltip=False):
        data = soup.find_all('table',
                             attrs={'class': "table-sm table table-bordered matches betting-table text-center"})

        for row in data:
            row_text = row.get_text()
            if row_text.startswith('Фора'):
                row_list = row_text.split()
                total_number = None
                for n in range(3, len(row_list)):
                    if n % 2:
                        total_number = row_list[n]
                    else:
                        if total_number:
                            all_coefficient_data[self.scrap_statistic_name(
                                soup=soup, tooltip=tooltip)][f'handicap_{row_list[1]}_&coefficient'].append(
                                {'total_number': total_number, 'coefficient': row_list[n]})
