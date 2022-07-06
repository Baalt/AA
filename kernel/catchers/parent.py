from kernel.printers.future import BetPrinter, TrainerPrinter, KushPrinter, LeaderBoardPrinter
from kernel.structures import HomeDataStructure, AwayDataStructure


class Catcher:
    def __init__(self,
                 home_structure: HomeDataStructure,
                 away_structure: AwayDataStructure,
                 big_match_data: dict,
                 coefficients: dict,
                 statistic_name: str,
                 all_league_data: dict):

        self.home_structure = home_structure
        self.away_structure = away_structure
        self.big_match_data = big_match_data
        self.coefficients = coefficients
        self.statistic_name = statistic_name
        self.all_league_data = all_league_data

    def total_calculation(self, coeff_set, seq: list):
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

            if coeff_under > 1.29:
                under_percent = (count_under * 100) / (count_over + count_under)

            if coeff_over > 1.29:
                over_percent = (count_over * 100) / (count_over + count_under)

            return under_percent, over_percent

        except Exception as err:
            print('rate_search Error: ', err)
            return None

    def handicap_calculation(self, coeff_set, current_seq: list, opposing_seq: list):
        if len(current_seq) == len(opposing_seq):
            win_list = []
            lose_list = []
            win_percent = None
            try:
                coeff_total = float(coeff_set['total_number'])
                coefficient = float(coeff_set['coefficient'])

                idx = 0
                for total in current_seq:
                    total_plus_handicap = (total + coeff_total) - opposing_seq[idx]  # current_seq.index(total)
                    idx += 1
                    # list_handicap.append(total_plus_handicap)
                    if total_plus_handicap > 0:
                        win_list.append(total)
                    elif total_plus_handicap < 0:
                        lose_list.append(total)

                count_win = len(win_list)
                count_lose = len(lose_list)

                if coefficient >= 1.29:
                    win_percent = (count_win * 100) / (count_win + count_lose)

                # print('Тотал и коэфф', coeff_total, coefficient)
                # print('кол-во игр', len(current_seq), len(opposing_seq))
                # print(list_handicap)
                # print(win_list)
                # print(lose_list)
                # print(count_win, count_lose)
                # print('Процент победы', win_percent)

                return win_percent

            except Exception as err:
                print('rate_search Error: ', err)
                return None
        return None

    def search_kush_rate(self,
                         statistic_name: str,
                         league_name: str,
                         coeff_set: dict,
                         rate_direction: str,
                         coeff_under_over_key: str,
                         ord_or_exp: int,
                         big_data_current_percent: float,
                         big_data_opposing_percent: float,
                         last_year_current_percent: float,
                         last_year_opposing_percent: float,
                         similar_current_percent: float,
                         similar_opposing_percent: float,
                         last_20_current_percent: float,
                         last_20_opposing_percent: float,
                         last_12_current_percent: float,
                         last_12_opposing_percent: float,
                         last_8_current_percent: float,
                         last_8_opposing_percent: float,
                         last_4_current_percent: float,
                         last_4_opposing_percent: float):
        try:
            last_20_percent = (last_20_current_percent + last_20_opposing_percent) / 2
            last_12_percent = (last_12_current_percent + last_12_opposing_percent) / 2
            last_8_percent = (last_8_current_percent + last_8_opposing_percent) / 2
            last_4_percent = (last_4_current_percent + last_4_opposing_percent) / 2
            similar_percent = (similar_current_percent + similar_opposing_percent) / 2
            big_data_percent = (big_data_current_percent + big_data_opposing_percent) / 2
            last_year_percent = (last_year_current_percent + last_year_opposing_percent) / 2

            big_data_kush_by_rate = self.kush_calculate(percent=big_data_percent,
                                                        coefficient=coeff_set[coeff_under_over_key])
            last_year_kush_by_rate = self.kush_calculate(percent=last_year_percent,
                                                         coefficient=coeff_set[coeff_under_over_key])
            similar_kush_by_rate = self.kush_calculate(percent=similar_percent,
                                                       coefficient=coeff_set[coeff_under_over_key])
            last_20_kush_by_rate = self.kush_calculate(percent=last_20_percent,
                                                       coefficient=coeff_set[coeff_under_over_key])
            last_12_kush_by_rate = self.kush_calculate(percent=last_12_percent,
                                                       coefficient=coeff_set[coeff_under_over_key])
            last_8_kush_by_rate = self.kush_calculate(percent=last_8_percent,
                                                      coefficient=coeff_set[coeff_under_over_key])
            last_4_kush_by_rate = self.kush_calculate(percent=last_4_percent,
                                                      coefficient=coeff_set[coeff_under_over_key])

            KushPrinter(statistic_name=statistic_name,
                        league_name=league_name,
                        big_data_percent=big_data_percent,
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
                        category='Kush+',
                        big_data_kush_by_rate=big_data_kush_by_rate,
                        last_year_kush_by_rate=last_year_kush_by_rate,
                        similar_kush_by_rate=similar_kush_by_rate,
                        last_20_kush_by_rate=last_20_kush_by_rate,
                        last_12_kush_by_rate=last_12_kush_by_rate,
                        last_8_kush_by_rate=last_8_kush_by_rate,
                        last_4_kush_by_rate=last_4_kush_by_rate).print_rate()
            TrainerPrinter(big_match_data=self.big_match_data).print_trainer_info()
            board_printer = LeaderBoardPrinter(all_league_data=self.all_league_data)
            board_printer.show_league_table()
            board_printer.show_current_static_table(statistic_name=statistic_name)

            if big_data_kush_by_rate and last_year_kush_by_rate and similar_kush_by_rate \
                    and last_20_kush_by_rate and last_12_kush_by_rate and last_8_kush_by_rate:
                min_kush = min(big_data_kush_by_rate, last_year_kush_by_rate, similar_kush_by_rate,
                               last_20_kush_by_rate, last_12_kush_by_rate, last_8_kush_by_rate)
                if min_kush >= 0.3:
                    KushPrinter(statistic_name=statistic_name,
                                league_name=league_name,
                                big_data_percent=big_data_percent,
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
                                category='Kush+',
                                big_data_kush_by_rate=big_data_kush_by_rate,
                                last_year_kush_by_rate=last_year_kush_by_rate,
                                similar_kush_by_rate=similar_kush_by_rate,
                                last_20_kush_by_rate=last_20_kush_by_rate,
                                last_12_kush_by_rate=last_12_kush_by_rate,
                                last_8_kush_by_rate=last_8_kush_by_rate,
                                last_4_kush_by_rate=last_4_kush_by_rate).print_rate()
                    TrainerPrinter(big_match_data=self.big_match_data).print_trainer_info()
                    board_printer = LeaderBoardPrinter(all_league_data=self.all_league_data)
                    board_printer.show_league_table()
                    if statistic_name != 'Голы':
                        board_printer.show_current_static_table(statistic_name=statistic_name)

            if similar_percent and last_20_percent and last_12_percent and last_8_percent and last_4_percent:
                if similar_percent >= ord_or_exp and last_20_percent >= ord_or_exp and last_12_percent > ord_or_exp:
                    if last_8_percent > 87.4 and last_4_percent > 99:
                        BetPrinter(statistic_name=statistic_name,
                                   league_name=league_name,
                                   big_data_percent=big_data_percent,
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
                                   category='B').print_rate()
                        TrainerPrinter(big_match_data=self.big_match_data).print_trainer_info()

        except Exception as err:
            print('search kush rate error: ', err)

    def is_there_a_weak_point(self,
                              statistic_name: str,
                              league_name: str,
                              coeff_set: dict,
                              rate_direction: str,
                              coeff_under_over_key: str,
                              ord_or_exp: int,
                              big_data_current_percent: float,
                              big_data_opposing_percent: float,
                              last_year_current_percent: float,
                              last_year_opposing_percent: float,
                              similar_current_percent: float,
                              similar_opposing_percent: float,
                              last_20_current_percent: float,
                              last_20_opposing_percent: float,
                              last_12_current_percent: float,
                              last_12_opposing_percent: float,
                              last_8_current_percent: float,
                              last_8_opposing_percent: float,
                              last_4_current_percent: float,
                              last_4_opposing_percent: float):

        self.search_kush_rate(statistic_name=statistic_name,
                              league_name=league_name,
                              coeff_set=coeff_set,
                              rate_direction=rate_direction,
                              coeff_under_over_key=coeff_under_over_key,
                              ord_or_exp=ord_or_exp,
                              big_data_current_percent=big_data_current_percent,
                              big_data_opposing_percent=big_data_opposing_percent,
                              last_year_current_percent=last_year_current_percent,
                              last_year_opposing_percent=last_year_opposing_percent,
                              similar_current_percent=similar_current_percent,
                              similar_opposing_percent=similar_opposing_percent,
                              last_20_current_percent=last_20_current_percent,
                              last_20_opposing_percent=last_20_opposing_percent,
                              last_12_current_percent=last_12_current_percent,
                              last_12_opposing_percent=last_12_opposing_percent,
                              last_8_current_percent=last_8_current_percent,
                              last_8_opposing_percent=last_8_opposing_percent,
                              last_4_current_percent=last_4_current_percent,
                              last_4_opposing_percent=last_4_opposing_percent)

        if similar_current_percent >= ord_or_exp and similar_opposing_percent >= ord_or_exp:
            similar_percent = (similar_current_percent + similar_opposing_percent) / 2
        else:
            similar_percent = None

        if last_20_current_percent >= ord_or_exp and last_20_opposing_percent >= ord_or_exp:
            last_20_percent = (last_20_current_percent + last_20_opposing_percent) / 2
        else:
            last_20_percent = None

        if last_12_current_percent >= ord_or_exp and last_12_opposing_percent >= ord_or_exp:
            last_12_percent = (last_12_current_percent + last_12_opposing_percent) / 2
        else:
            last_12_percent = None

        if last_8_current_percent > 87.4 and last_8_opposing_percent > 87.4:
            last_8_percent = (last_8_current_percent + last_8_opposing_percent) / 2
        else:
            last_8_percent = None

        if last_4_current_percent > 99 and last_4_opposing_percent > 99:
            last_4_percent = (last_4_current_percent + last_4_opposing_percent) / 2
        else:
            last_4_percent = None

        if similar_percent and last_20_percent and last_12_percent and last_8_percent and last_4_percent:
            big_data_percent = (big_data_current_percent + big_data_opposing_percent) / 2
            last_year_percent = (last_year_current_percent + last_year_opposing_percent) / 2
            BetPrinter(statistic_name=statistic_name,
                       league_name=league_name,
                       big_data_percent=big_data_percent,
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
                       category='A').print_rate()
            TrainerPrinter(big_match_data=self.big_match_data).print_trainer_info()
            board_printer = LeaderBoardPrinter(all_league_data=self.all_league_data)
            board_printer.show_league_table()
            board_printer.show_current_static_table(statistic_name=statistic_name)

    def kush_calculate(self, percent, coefficient):
        if not isinstance(percent, float):
            percent = float(percent)
        if not isinstance(coefficient, float):
            coefficient = float(coefficient)
        if percent > 0 and percent <= 100:
            kush = ((percent * (coefficient - 1)) - (100 - percent)) / 100
            return kush
        return None
        # print('Big Data', big_data_percent, big_data_current_percent, big_data_opposing_percent)
        # print('Last Year', last_year_percent, last_year_current_percent, last_year_opposing_percent)
        # print('Similar', similar_percent, similar_current_percent, similar_opposing_percent)
        # print('last20', last_20_percent, last_20_current_percent, last_20_opposing_percent)
        # print('last12', last_12_percent, last_12_current_percent, last_12_opposing_percent)
        # print('last8', last_8_percent, last_8_current_percent, last_8_opposing_percent)
        # print('last4', last_4_percent, last_4_current_percent, last_4_opposing_percent)
