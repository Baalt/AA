from kernel.printers.future import BetPrinter
from kernel.structures import HomeDataStructure, AwayDataStructure


class Catcher:
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

            # print(len(seq))
            # print(seq)
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
                    total_plus_handicap = (total + coeff_total) - opposing_seq[idx] #current_seq.index(total)
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


        else:

            try:
                last_20_percent = (last_20_current_percent + last_20_opposing_percent) / 2
                last_12_percent = (last_12_current_percent + last_12_opposing_percent) / 2
                last_8_percent = (last_8_current_percent + last_8_opposing_percent) / 2
                last_4_percent = (last_4_current_percent + last_4_opposing_percent) / 2
                similar_percent = (similar_current_percent + similar_opposing_percent) / 2
            except Exception as err:
                print(err)
                similar_percent = None
                last_20_percent = None
                last_12_percent = None
                last_8_percent = None
                last_4_percent = None

            if similar_percent and last_20_percent and last_12_percent and last_8_percent and last_4_percent:
                if similar_percent >= ord_or_exp and last_20_percent >= ord_or_exp and last_12_percent > ord_or_exp:
                    if last_8_percent > 87.4 and last_4_percent > 99:
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
                                   category='B').print_rate()


            # print('Big Data', big_data_percent, big_data_current_percent, big_data_opposing_percent)
            # print('Last Year', last_year_percent, last_year_current_percent, last_year_opposing_percent)
            # print('Similar', similar_percent, similar_current_percent, similar_opposing_percent)
            # print('last20', last_20_percent, last_20_current_percent, last_20_opposing_percent)
            # print('last12', last_12_percent, last_12_current_percent, last_12_opposing_percent)
            # print('last8', last_8_percent, last_8_current_percent, last_8_opposing_percent)
            # print('last4', last_4_percent, last_4_current_percent, last_4_opposing_percent)



