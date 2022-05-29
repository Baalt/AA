from bs4 import BeautifulSoup


class LiveDataStructure:
    def __init__(self):
        self.total_sets = []
        self.current_individual_total_sets = []
        self.opposing_individual_total_sets = []
        self.current_handicap_sets = []
        self.opposing_handicap_sets = []


class LiveScraper:
    def __init__(self):
        self.home_set = LiveDataStructure()
        self.away_set = LiveDataStructure()

    def scrap(self, soup: BeautifulSoup):
        tables = soup.find_all('div', {'class': "card-body"})
        if len(tables) == 8:
            home_tables = tables[4]
            away_tables = tables[6]
            home_data_container = home_tables.find_all('div', {'class': "col px-1"})
            away_data_container = away_tables.find_all('div', {'class': "col px-1"})
            self.scrap_to_structure(set=self.home_set, data_container=home_data_container)
            self.scrap_to_structure(set=self.away_set, data_container=away_data_container)
            result_set = self.from_data_to_db()
            return result_set
        raise AttributeError

    def from_data_to_db(self):
        total_over = None
        total_over_percent = None
        total_under = None
        total_under_percent = None

        home_individual_over = None
        home_individual_over_percent = None
        home_individual_under = None
        home_individual_under_percent = None

        away_individual_over = None
        away_individual_over_percent = None
        away_individual_under = None
        away_individual_under_percent = None

        home_handicap_result = None
        home_handicap_result_percent = None
        away_handicap_result = None
        away_handicap_result_percent = None

        for home_set in self.home_set.total_sets:
            home_total, home_TO, home_TU = home_set
            home_TO, home_TO_match_count = home_TO.split('/')
            home_TU, home_TU_match_count = home_TU.split('/')
            home_TO, home_TU, home_TO_match_count = int(home_TO), int(home_TU), int(home_TO_match_count)
            if home_TO_match_count >= 60:
                for away_set in self.away_set.total_sets:
                    away_total, away_TO, away_TU = away_set
                    if home_total == away_total:
                        away_TO, away_TO_match_count = away_TO.split('/')
                        away_TU, away_TU_match_count = away_TU.split('/')
                        away_TO, away_TU, away_TO_match_count = int(away_TO), int(away_TU), int(away_TO_match_count)
                        if away_TO_match_count >= 60:
                            TO = (home_TO + away_TO) / 2
                            TU = (home_TU + away_TU) / 2
                            if TO > 89:
                                if total_over:
                                    if total_over_percent > TO:
                                        total_over_percent = TO
                                        total_over = home_total
                                else:
                                    total_over_percent = TO
                                    total_over = home_total

                            if TU > 89:
                                if total_under:
                                    if total_under_percent > TU:
                                        total_under_percent = TU
                                        total_under = home_total
                                else:
                                    total_under_percent = TU
                                    total_under = home_total

                        else:
                            raise AttributeError

            else:
                raise AttributeError

        # print('Total Over&% ', total_over, total_over_percent, '%')
        # print('Total Under&% ', total_under, total_under_percent, '%')

        for home_set in self.home_set.current_individual_total_sets:
            home_total, home_TO, home_TU = home_set
            home_TO, home_TO_match_count = home_TO.split('/')
            home_TU, home_TU_match_count = home_TU.split('/')
            home_TO, home_TU, home_TO_match_count = int(home_TO), int(home_TU), int(home_TO_match_count)
            if home_TO_match_count >= 60:
                for away_set in self.away_set.opposing_individual_total_sets:
                    away_total, away_TO, away_TU = away_set
                    if home_total == away_total:
                        away_TO, away_TO_match_count = away_TO.split('/')
                        away_TU, away_TU_match_count = away_TU.split('/')
                        away_TO, away_TU, away_TO_match_count = int(away_TO), int(away_TU), int(away_TO_match_count)
                        if away_TO_match_count >= 60:
                            TO = (home_TO + away_TO) / 2
                            TU = (home_TU + away_TU) / 2
                            if TO > 89:
                                if home_individual_over:
                                    if home_individual_over_percent > TO:
                                        home_individual_over_percent = TO
                                        home_individual_over = home_total
                                else:
                                    home_individual_over_percent = TO
                                    home_individual_over = home_total

                            if TU > 89:
                                if home_individual_under:
                                    if home_individual_under_percent > TU:
                                        home_individual_under_percent = TU
                                        home_individual_under = home_total
                                else:
                                    home_individual_under_percent = TU
                                    home_individual_under = home_total

        # print('Home individual total Over&% ', home_individual_over, home_individual_over_percent, '%')
        # print('Home individual total Under&% ', home_individual_under, home_individual_under_percent, '%')

        for away_set in self.away_set.current_individual_total_sets:
            away_total, away_TO, away_TU = away_set
            away_TO, away_TO_match_count = away_TO.split('/')
            away_TU, away_TU_match_count = away_TU.split('/')
            away_TO, away_TU, away_TO_match_count = int(away_TO), int(away_TU), int(away_TO_match_count)
            if away_TO_match_count >= 60:
                for home_set in self.home_set.opposing_individual_total_sets:
                    home_total, home_TO, home_TU = home_set
                    if away_total == home_total:
                        home_TO, home_TO_match_count = home_TO.split('/')
                        home_TU, home_TU_match_count = home_TU.split('/')
                        home_TO, home_TU, home_TO_match_count = int(home_TO), int(home_TU), int(home_TO_match_count)
                        if home_TO_match_count >= 60:
                            TO = (home_TO + away_TO) / 2
                            TU = (home_TU + away_TU) / 2
                            if TO > 89:
                                if away_individual_over:
                                    if away_individual_over_percent > TO:
                                        away_individual_over_percent = TO
                                        away_individual_over = home_total
                                else:
                                    away_individual_over_percent = TO
                                    away_individual_over = home_total

                            if TU > 89:
                                if away_individual_under:
                                    if away_individual_under_percent > TU:
                                        away_individual_under_percent = TU
                                        away_individual_under = home_total
                                else:
                                    away_individual_under_percent = TU
                                    away_individual_under = home_total

        # print('Away individual total Over&% ', away_individual_over, away_individual_over_percent, '%')
        # print('Away individual total Under&% ', away_individual_under, away_individual_under_percent, '%')

        for home_handicap_set in self.home_set.current_handicap_sets:
            home_handicap, home_handicap_percent_set = home_handicap_set
            home_handicap_percent, home_handicap_match_count = home_handicap_percent_set.split('/')
            home_handicap_percent, home_handicap_match_count = int(home_handicap_percent), int(
                home_handicap_match_count)
            if home_handicap_match_count >= 60:
                for away_handicap_set in self.away_set.opposing_handicap_sets:
                    away_handicap, away_handicap_percent_set = away_handicap_set
                    if home_handicap == away_handicap:
                        away_handicap_percent, away_handicap_match_count = away_handicap_percent_set.split('/')
                        away_handicap_percent, away_handicap_match_count = int(away_handicap_percent), int(
                            away_handicap_match_count)
                        if away_handicap_match_count >= 60:
                            home_handicap_percent = int(home_handicap_percent)
                            away_handicap_percent = int(away_handicap_percent)
                            handicap_percent = (home_handicap_percent + away_handicap_percent) / 2
                            if handicap_percent > 89:
                                if home_handicap_result_percent:
                                    if home_handicap_result_percent > handicap_percent:
                                        home_handicap_result_percent = handicap_percent
                                        home_handicap_result = home_handicap
                                else:
                                    home_handicap_result_percent = handicap_percent
                                    home_handicap_result = home_handicap

        # print('Home handicap T&% ', home_handicap_result, home_handicap_result_percent)

        for away_handicap_set in self.away_set.current_handicap_sets:
            away_handicap, away_handicap_percent_set = away_handicap_set
            away_handicap_percent, away_handicap_match_count = away_handicap_percent_set.split('/')
            away_handicap_percent, away_handicap_match_count = int(away_handicap_percent), int(
                away_handicap_match_count)
            if away_handicap_match_count >= 60:
                for home_handicap_set in self.home_set.opposing_handicap_sets:
                    home_handicap, home_handicap_percent_set = home_handicap_set
                    if away_handicap == home_handicap:
                        home_handicap_percent, home_handicap_match_count = home_handicap_percent_set.split('/')
                        home_handicap_percent, home_handicap_match_count = int(home_handicap_percent), int(
                            home_handicap_match_count)
                        if home_handicap_match_count >= 60:
                            home_handicap_percent = int(home_handicap_percent)
                            away_handicap_percent = int(away_handicap_percent)
                            handicap_percent = (home_handicap_percent + away_handicap_percent) / 2
                            if handicap_percent > 89:
                                if away_handicap_result_percent:
                                    if away_handicap_result_percent > handicap_percent:
                                        away_handicap_result_percent = handicap_percent
                                        away_handicap_result = away_handicap
                                else:
                                    away_handicap_result_percent = handicap_percent
                                    away_handicap_result = away_handicap

        # print('Away handicap T&% ', away_handicap_result, away_handicap_result_percent)
        return {'TO': total_over, 'TO%': total_over_percent,
                'TU': total_under, "TU%": total_under_percent,
                'home_TO': home_individual_over, 'home_TO%': home_individual_over_percent,
                'home_TU': home_individual_under, 'home_TU%': home_individual_under_percent,
                'away_TO': away_individual_over, 'away_TO%': away_individual_over_percent,
                'away_TU': away_individual_under, 'away_TU%': away_individual_under_percent,
                'home_handicap': home_handicap_result, 'home_handicap%': home_handicap_result_percent,
                'away_handicap': away_handicap_result, 'away_handicap%': away_handicap_result_percent}

    def scrap_to_structure(self, set, data_container):
        for data in data_container[0].find('tbody').find_all('tr'):
            set.total_sets.append(data.get_text().split())
        for data in data_container[1].find('tbody').find_all('tr'):
            set.current_individual_total_sets.append(data.get_text().split())
        for data in data_container[2].find('tbody').find_all('tr'):
            set.opposing_individual_total_sets.append(data.get_text().split())
        for data in data_container[3].find('tbody').find_all('tr'):
            set.current_handicap_sets.append(data.get_text().split())
        for data in data_container[4].find('tbody').find_all('tr'):
            set.opposing_handicap_sets.append(data.get_text().split())
