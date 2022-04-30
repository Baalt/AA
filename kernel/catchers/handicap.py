from kernel.catchers.parent import Catcher


class HandicapCatcher(Catcher):
    def search_handicap_1_rate(self, statistic_name: str):
        for coeff_set in self.coefficients[self.statistic_name]['handicap_1_&coefficient']:
            big_data_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    big_data_individual_total_current_home_in_home_away_games,
                opposing_seq=self.home_structure.
                    big_data_individual_total_opposing_teams_current_home_in_home_away_games)

            big_data_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    big_data_individual_total_opposing_teams_current_away_in_home_away_games,
                opposing_seq=self.away_structure.
                    big_data_individual_total_current_away_in_home_away_games)

            last_year_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_year_individual_total_current_home_command_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_year_individual_total_opposing_teams_current_home_in_home_away_games)

            last_year_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_year_individual_total_opposing_teams_current_away_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_year_individual_total_current_away_command_in_home_away_games)

            similar_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    similar_command_individual_total_current_home_command_in_home_away_games,
                opposing_seq=self.home_structure.
                    similar_command_individual_total_opposing_teams_current_home_in_home_away_games)

            similar_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    similar_command_individual_total_opposing_teams_current_away_in_home_away_games,
                opposing_seq=self.away_structure.
                    similar_command_individual_total_current_away_command_in_home_away_games)

            last_20_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_20_games_individual_total_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            last_20_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_20_games_individual_total_current_away_by_year_in_home_away_games)

            last_12_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_12_games_individual_total_current_home_by_year_in_home_games,
                opposing_seq=self.home_structure.
                    last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games)

            last_12_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games,
                opposing_seq=self.away_structure.
                    last_12_games_individual_total_current_away_by_year_in_away_games)

            last_8_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_8_games_individual_total_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            last_8_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_8_games_individual_total_current_away_by_year_in_home_away_games)

            last_4_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_4_games_individual_total_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            last_4_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_4_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_4_games_individual_total_current_away_by_year_in_home_away_games)

            if big_data_current_percent and big_data_opposing_percent and \
                    last_year_current_percent and last_year_opposing_percent and \
                    similar_current_percent and similar_opposing_percent and \
                    last_20_current_percent and last_20_opposing_percent and \
                    last_12_current_percent and last_12_opposing_percent and \
                    last_8_current_percent and last_8_opposing_percent and \
                    last_4_current_percent and last_4_opposing_percent:
                if float(coeff_set['coefficient']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Handicap 1',
                                               coeff_under_over_key='coefficient',
                                               ord_or_exp=68,
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

                if float(coeff_set['coefficient']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Handicap 1',
                                               coeff_under_over_key='coefficient',
                                               ord_or_exp=85,
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

    def search_handicap_2_rate(self, statistic_name: str):
        for coeff_set in self.coefficients[self.statistic_name]['handicap_2_&coefficient']:
            big_data_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    big_data_individual_total_current_away_in_home_away_games,
                opposing_seq=self.away_structure.
                    big_data_individual_total_opposing_teams_current_away_in_home_away_games)

            big_data_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    big_data_individual_total_opposing_teams_current_home_in_home_away_games,
                opposing_seq=self.home_structure.
                    big_data_individual_total_current_home_in_home_away_games)

            last_year_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_year_individual_total_current_away_command_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_year_individual_total_opposing_teams_current_away_in_home_away_games)

            last_year_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_year_individual_total_opposing_teams_current_home_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_year_individual_total_current_home_command_in_home_away_games)

            similar_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    similar_command_individual_total_current_away_command_in_home_away_games,
                opposing_seq=self.away_structure.
                    similar_command_individual_total_opposing_teams_current_away_in_home_away_games)

            similar_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    similar_command_individual_total_opposing_teams_current_home_in_home_away_games,
                opposing_seq=self.home_structure.
                    similar_command_individual_total_current_home_command_in_home_away_games)

            last_20_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_20_games_individual_total_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

            last_20_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_20_games_individual_total_current_home_by_year_in_home_away_games)

            last_12_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_12_games_individual_total_current_away_by_year_in_away_games,
                opposing_seq=self.away_structure.
                    last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games)

            last_12_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games,
                opposing_seq=self.home_structure.
                    last_12_games_individual_total_current_home_by_year_in_home_games)

            last_8_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_8_games_individual_total_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

            last_8_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_8_games_individual_total_current_home_by_year_in_home_away_games)

            last_4_current_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.away_structure.
                    last_4_games_individual_total_current_away_by_year_in_home_away_games,
                opposing_seq=self.away_structure.
                    last_4_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

            last_4_opposing_percent = self.handicap_calculation(
                coeff_set=coeff_set,
                current_seq=self.home_structure.
                    last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games,
                opposing_seq=self.home_structure.
                    last_4_games_individual_total_current_home_by_year_in_home_away_games)

            if big_data_current_percent and big_data_opposing_percent and \
                    last_year_current_percent and last_year_opposing_percent and \
                    similar_current_percent and similar_opposing_percent and \
                    last_20_current_percent and last_20_opposing_percent and \
                    last_12_current_percent and last_12_opposing_percent and \
                    last_8_current_percent and last_8_opposing_percent and \
                    last_4_current_percent and last_4_opposing_percent:

                if float(coeff_set['coefficient']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Handicap 2',
                                               coeff_under_over_key='coefficient',
                                               ord_or_exp=68,
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

                if float(coeff_set['coefficient']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Handicap 2',
                                               coeff_under_over_key='coefficient',
                                               ord_or_exp=85,
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
