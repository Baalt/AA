from kernel.printers.future import BetPrinter
from kernel.structures import HomeDataStructure, AwayDataStructure


class TotalCatcher:
    def __init__(self,
                 home_structure: HomeDataStructure,
                 away_structure: AwayDataStructure,
                 big_match_data: dict,
                 coefficients: dict,
                 statistic_name: str):

        self.home_structure = home_structure
        self.away_structure = away_structure
        self.big_match_data = big_match_data
        self.coefficients = coefficients
        self.statistic_name = statistic_name

    def search_total_rate(self):
        for coeff_set in self.coefficients[self.statistic_name]['total&coefficient']:
            big_data_home_result = self.calculations(coeff_set=coeff_set,
                                                     seq=self.home_structure.
                                                     big_data_total_current_home_in_home_away_games)
            big_data_away_result = self.calculations(coeff_set=coeff_set,
                                                     seq=self.away_structure.
                                                     big_data_total_current_away_in_home_away_games)

            last_year_home_result = self.calculations(coeff_set=coeff_set,
                                                      seq=self.home_structure.
                                                      last_year_total_current_home_command_in_home_away_games)
            last_year_away_result = self.calculations(coeff_set=coeff_set,
                                                      seq=self.away_structure.
                                                      last_year_total_current_away_command_in_home_away_games)

            similar_home_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.home_structure.
                                                    similar_command_total_current_home_big_data_home_away_games)
            similar_away_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.away_structure.
                                                    similar_command_total_current_away_big_data_home_away_games)

            last_20_home_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.home_structure.
                                                    last_20_games_total_current_home_by_year_in_home_away_games)
            last_20_away_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.away_structure.
                                                    last_20_games_total_current_away_by_year_in_home_away_games)

            last_12_home_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.home_structure.
                                                    last_12_games_total_current_home_command_by_year_in_home_games[:12])
            last_12_away_result = self.calculations(coeff_set=coeff_set,
                                                    seq=self.away_structure.
                                                    last_12_games_total_current_away_command_by_year_in_away_games[:12])

            last_8_home_result = self.calculations(coeff_set=coeff_set,
                                                   seq=self.home_structure.
                                                   last_8_games_total_current_home_by_year_in_home_away_games)
            last_8_away_result = self.calculations(coeff_set=coeff_set,
                                                   seq=self.away_structure.
                                                   last_8_games_total_current_away_by_year_in_home_away_games)

            last_4_home_result = self.calculations(coeff_set=coeff_set,
                                                   seq=self.home_structure.
                                                   last_4_games_total_current_home_by_year_in_home_away_games)
            last_4_away_result = self.calculations(coeff_set=coeff_set,
                                                   seq=self.away_structure.
                                                   last_4_games_total_current_away_by_year_in_home_away_games)

            if big_data_home_result and big_data_away_result:
                big_data_home_under_percent, big_data_home_over_percent = big_data_home_result
                big_data_away_under_percent, big_data_away_over_percent = big_data_away_result

                last_year_home_under_percent, last_year_home_over_percent = last_year_home_result
                last_year_away_under_percent, last_year_away_over_percent = last_year_away_result

                similar_home_under_percent, similar_home_over_percent = similar_home_result
                similar_away_under_percent, similar_away_over_percent = similar_away_result

                last_20_home_under_percent, last_20_home_over_percent = last_20_home_result
                last_20_away_under_percent, last_20_away_over_percent = last_20_away_result

                last_12_home_under_percent, last_12_home_over_percent = last_12_home_result
                last_12_away_under_percent, last_12_away_over_percent = last_12_away_result

                last_8_home_under_percent, last_8_home_over_percent = last_8_home_result
                last_8_away_under_percent, last_8_away_over_percent = last_8_away_result

                last_4_home_under_percent, last_4_home_over_percent = last_4_home_result
                last_4_away_under_percent, last_4_away_over_percent = last_4_away_result

                if big_data_home_under_percent and big_data_away_under_percent and \
                        coeff_set['coefficient_under'] >= 1.683:
                    self.is_there_a_weak_point(coeff_set=coeff_set,
                                               rate_direction='Total Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=75,
                                               big_data_home_percent=big_data_home_under_percent,
                                               big_data_away_percent=big_data_away_under_percent,
                                               last_year_home_percent=last_year_home_under_percent,
                                               last_year_away_percent=last_year_away_under_percent,
                                               similar_home_percent=similar_home_under_percent,
                                               similar_away_percent=similar_away_under_percent,
                                               last_20_home_percent=last_20_home_under_percent,
                                               last_20_away_percent=last_20_away_under_percent,
                                               last_12_home_percent=last_12_home_under_percent,
                                               last_12_away_percent=last_12_away_under_percent,
                                               last_8_home_percent=last_8_home_under_percent,
                                               last_8_away_percent=last_8_away_under_percent,
                                               last_4_home_percent=last_4_home_under_percent,
                                               last_4_away_percent=last_4_away_under_percent)

                if big_data_home_under_percent and big_data_away_under_percent and \
                        coeff_set['coefficient_under'] < 1.683:
                    self.is_there_a_weak_point(coeff_set=coeff_set,
                                               rate_direction='Total Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=88,
                                               big_data_home_percent=big_data_home_under_percent,
                                               big_data_away_percent=big_data_away_under_percent,
                                               last_year_home_percent=last_year_home_under_percent,
                                               last_year_away_percent=last_year_away_under_percent,
                                               similar_home_percent=similar_home_under_percent,
                                               similar_away_percent=similar_away_under_percent,
                                               last_20_home_percent=last_20_home_under_percent,
                                               last_20_away_percent=last_20_away_under_percent,
                                               last_12_home_percent=last_12_home_under_percent,
                                               last_12_away_percent=last_12_away_under_percent,
                                               last_8_home_percent=last_8_home_under_percent,
                                               last_8_away_percent=last_8_away_under_percent,
                                               last_4_home_percent=last_4_home_under_percent,
                                               last_4_away_percent=last_4_away_under_percent)

                if big_data_home_over_percent and big_data_away_over_percent and \
                        coeff_set['coefficient_over'] >= 1.683:
                    self.is_there_a_weak_point(coeff_set=coeff_set,
                                               rate_direction='Total Over',
                                               coeff_under_over_key='coefficient_over',
                                               ord_or_exp=75,
                                               big_data_home_percent=big_data_home_over_percent,
                                               big_data_away_percent=big_data_away_over_percent,
                                               last_year_home_percent=last_year_home_over_percent,
                                               last_year_away_percent=last_year_away_over_percent,
                                               similar_home_percent=similar_home_over_percent,
                                               similar_away_percent=similar_away_over_percent,
                                               last_20_home_percent=last_20_home_over_percent,
                                               last_20_away_percent=last_20_away_over_percent,
                                               last_12_home_percent=last_12_home_over_percent,
                                               last_12_away_percent=last_12_away_over_percent,
                                               last_8_home_percent=last_8_home_over_percent,
                                               last_8_away_percent=last_8_away_over_percent,
                                               last_4_home_percent=last_4_home_over_percent,
                                               last_4_away_percent=last_4_away_over_percent)

                    if big_data_home_over_percent and big_data_away_over_percent and \
                            coeff_set['coefficient_over'] < 1.683:
                        self.is_there_a_weak_point(coeff_set=coeff_set,
                                                   rate_direction='Total Over',
                                                   coeff_under_over_key='coefficient_over',
                                                   ord_or_exp=88,
                                                   big_data_home_percent=big_data_home_over_percent,
                                                   big_data_away_percent=big_data_away_over_percent,
                                                   last_year_home_percent=last_year_home_over_percent,
                                                   last_year_away_percent=last_year_away_over_percent,
                                                   similar_home_percent=similar_home_over_percent,
                                                   similar_away_percent=similar_away_over_percent,
                                                   last_20_home_percent=last_20_home_over_percent,
                                                   last_20_away_percent=last_20_away_over_percent,
                                                   last_12_home_percent=last_12_home_over_percent,
                                                   last_12_away_percent=last_12_away_over_percent,
                                                   last_8_home_percent=last_8_home_over_percent,
                                                   last_8_away_percent=last_8_away_over_percent,
                                                   last_4_home_percent=last_4_home_over_percent,
                                                   last_4_away_percent=last_4_away_over_percent)

    def calculations(self, coeff_set, seq):
        over_list = []
        under_list = []
        under_percent, over_percent = None, None
        try:
            coeff_total = float(coeff_set['total_number'])
            coeff_under = float(coeff_set['coefficient_under'])
            coeff_over = float(coeff_set['coefficient_over'])

            for total in seq:
                if total > coeff_total:
                    over_list.append(total)
                elif total < coeff_total:
                    under_list.append(total)

                count_under = len(under_list)
                count_over = len(over_list)

                if coeff_under > 1.3:
                    under_percent = (count_under * 100) / (count_over + count_under)

                if coeff_over > 1.3:
                    over_percent = (count_over * 100) / (count_over + count_under)

            return under_percent, over_percent

        except Exception as err:
            print('rate_search Error: ', err)
            return None

    def is_there_a_weak_point(self,
                              coeff_set: dict,
                              rate_direction: str,
                              coeff_under_over_key: str,
                              ord_or_exp: int,
                              big_data_home_percent: float,
                              big_data_away_percent: float,
                              last_year_home_percent: float,
                              last_year_away_percent: float,
                              similar_home_percent: float,
                              similar_away_percent: float,
                              last_20_home_percent: float,
                              last_20_away_percent: float,
                              last_12_home_percent: float,
                              last_12_away_percent: float,
                              last_8_home_percent: float,
                              last_8_away_percent: float,
                              last_4_home_percent: float,
                              last_4_away_percent: float):

        if similar_home_percent >= ord_or_exp and similar_away_percent >= ord_or_exp:
            similar_percent = (similar_home_percent + similar_away_percent) / 2
        else:
            similar_percent = None

        if last_20_home_percent >= ord_or_exp and last_20_away_percent >= ord_or_exp:
            last_20_percent = (last_20_home_percent + last_20_away_percent) / 2
        else:
            last_20_percent = None

        if last_12_home_percent >= ord_or_exp and last_12_away_percent >= ord_or_exp:
            last_12_percent = (last_12_home_percent + last_12_away_percent) / 2
        else:
            last_12_percent = None

        if last_8_home_percent > 87.4 and last_8_away_percent > 87.4:
            last_8_percent = (last_8_home_percent + last_8_away_percent) / 2
        else:
            last_8_percent = None

        if last_4_home_percent > 99 and last_4_away_percent > 99:
            last_4_percent = (last_4_home_percent + last_4_away_percent) / 2
        else:
            last_4_percent = None

        if similar_percent and last_20_percent and last_12_percent and last_8_percent and last_4_percent:
            big_data_percent = (big_data_home_percent + big_data_away_percent) / 2
            last_year_percent = (last_year_home_percent + last_year_away_percent) / 2

            BetPrinter(big_data_percent=big_data_percent,
                       last_year_percent=last_year_percent,
                       similar_percent=similar_percent,
                       last_20_percent=last_20_percent,
                       last_12_percent=last_12_percent,
                       last_8_percent=last_8_percent,
                       last_4_percent=last_4_percent,
                       big_match_data=self.big_match_data,
                       coeff_total=coeff_set['total_number'],
                       coeff_value=coeff_set[coeff_under_over_key],
                       rate_direction=rate_direction,
                       ord_or_exp=ord_or_exp).print_rate()
