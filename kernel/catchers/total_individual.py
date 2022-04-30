from kernel.catchers.parent import Catcher


class IndividualTotalCatcher(Catcher):
    def search_individual_1_total_rate(self, statistic_name: str):
        for coeff_set in self.coefficients[self.statistic_name]['total_1_&coefficient']:
            big_data_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    big_data_individual_total_current_home_in_home_away_games)
            big_data_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    big_data_individual_total_opposing_teams_current_away_in_home_away_games)

            last_year_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_year_individual_total_current_home_command_in_home_away_games)
            last_year_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_year_individual_total_opposing_teams_current_away_in_home_away_games)

            similar_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    similar_command_individual_total_current_home_command_in_home_away_games)
            similar_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    similar_command_individual_total_opposing_teams_current_away_in_home_away_games)

            last_20_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_20_games_individual_total_current_home_by_year_in_home_away_games)
            last_20_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

            last_12_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                        last_12_games_individual_total_current_home_by_year_in_home_games[:12])
            last_12_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                        last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games[:12])

            last_8_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_8_games_individual_total_current_home_by_year_in_home_away_games)
            last_8_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

            last_4_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_4_games_total_current_home_by_year_in_home_away_games)
            last_4_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_4_games_total_current_away_by_year_in_home_away_games)

            if big_data_current_result and big_data_opposing_result:
                big_data_current_under_percent, big_data_current_over_percent = big_data_current_result
                big_data_opposing_under_percent, big_data_opposing_over_percent = big_data_opposing_result

                last_year_current_under_percent, last_year_current_over_percent = last_year_current_result
                last_year_opposing_under_percent, last_year_opposing_over_percent = last_year_opposing_result

                similar_current_under_percent, similar_current_over_percent = similar_current_result
                similar_opposing_under_percent, similar_opposing_over_percent = similar_opposing_result

                last_20_current_under_percent, last_20_current_over_percent = last_20_current_result
                last_20_opposing_under_percent, last_20_opposing_over_percent = last_20_opposing_result

                last_12_current_under_percent, last_12_current_over_percent = last_12_current_result
                last_12_opposing_under_percent, last_12_opposing_over_percent = last_12_opposing_result

                last_8_current_under_percent, last_8_current_over_percent = last_8_current_result
                last_8_opposing_under_percent, last_8_opposing_over_percent = last_8_opposing_result

                last_4_current_under_percent, last_4_current_over_percent = last_4_current_result
                last_4_opposing_under_percent, last_4_opposing_over_percent = last_4_opposing_result

                if big_data_current_under_percent and big_data_opposing_under_percent and \
                        float(coeff_set['coefficient_under']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 1 Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=68,
                                               big_data_current_percent=big_data_current_under_percent,
                                               big_data_opposing_percent=big_data_opposing_under_percent,
                                               last_year_current_percent=last_year_current_under_percent,
                                               last_year_opposing_percent=last_year_opposing_under_percent,
                                               similar_current_percent=similar_current_under_percent,
                                               similar_opposing_percent=similar_opposing_under_percent,
                                               last_20_current_percent=last_20_current_under_percent,
                                               last_20_opposing_percent=last_20_opposing_under_percent,
                                               last_12_current_percent=last_12_current_under_percent,
                                               last_12_opposing_percent=last_12_opposing_under_percent,
                                               last_8_current_percent=last_8_current_under_percent,
                                               last_8_opposing_percent=last_8_opposing_under_percent,
                                               last_4_current_percent=last_4_current_under_percent,
                                               last_4_opposing_percent=last_4_opposing_under_percent)

                if big_data_current_under_percent and big_data_opposing_under_percent and \
                        float(coeff_set['coefficient_under']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 1 Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=85,
                                               big_data_current_percent=big_data_current_under_percent,
                                               big_data_opposing_percent=big_data_opposing_under_percent,
                                               last_year_current_percent=last_year_current_under_percent,
                                               last_year_opposing_percent=last_year_opposing_under_percent,
                                               similar_current_percent=similar_current_under_percent,
                                               similar_opposing_percent=similar_opposing_under_percent,
                                               last_20_current_percent=last_20_current_under_percent,
                                               last_20_opposing_percent=last_20_opposing_under_percent,
                                               last_12_current_percent=last_12_current_under_percent,
                                               last_12_opposing_percent=last_12_opposing_under_percent,
                                               last_8_current_percent=last_8_current_under_percent,
                                               last_8_opposing_percent=last_8_opposing_under_percent,
                                               last_4_current_percent=last_4_current_under_percent,
                                               last_4_opposing_percent=last_4_opposing_under_percent)

                if big_data_current_over_percent and big_data_opposing_over_percent and \
                        float(coeff_set['coefficient_over']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 1 Over',
                                               coeff_under_over_key='coefficient_over',
                                               ord_or_exp=68,
                                               big_data_current_percent=big_data_current_over_percent,
                                               big_data_opposing_percent=big_data_opposing_over_percent,
                                               last_year_current_percent=last_year_current_over_percent,
                                               last_year_opposing_percent=last_year_opposing_over_percent,
                                               similar_current_percent=similar_current_over_percent,
                                               similar_opposing_percent=similar_opposing_over_percent,
                                               last_20_current_percent=last_20_current_over_percent,
                                               last_20_opposing_percent=last_20_opposing_over_percent,
                                               last_12_current_percent=last_12_current_over_percent,
                                               last_12_opposing_percent=last_12_opposing_over_percent,
                                               last_8_current_percent=last_8_current_over_percent,
                                               last_8_opposing_percent=last_8_opposing_over_percent,
                                               last_4_current_percent=last_4_current_over_percent,
                                               last_4_opposing_percent=last_4_opposing_over_percent)

                if big_data_current_over_percent and big_data_opposing_over_percent and \
                        float(coeff_set['coefficient_over']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 1 Over',
                                               coeff_under_over_key='coefficient_over',
                                               ord_or_exp=85,
                                               big_data_current_percent=big_data_current_over_percent,
                                               big_data_opposing_percent=big_data_opposing_over_percent,
                                               last_year_current_percent=last_year_current_over_percent,
                                               last_year_opposing_percent=last_year_opposing_over_percent,
                                               similar_current_percent=similar_current_over_percent,
                                               similar_opposing_percent=similar_opposing_over_percent,
                                               last_20_current_percent=last_20_current_over_percent,
                                               last_20_opposing_percent=last_20_opposing_over_percent,
                                               last_12_current_percent=last_12_current_over_percent,
                                               last_12_opposing_percent=last_12_opposing_over_percent,
                                               last_8_current_percent=last_8_current_over_percent,
                                               last_8_opposing_percent=last_8_opposing_over_percent,
                                               last_4_current_percent=last_4_current_over_percent,
                                               last_4_opposing_percent=last_4_opposing_over_percent)

    def search_individual_2_total_rate(self, statistic_name: str):
        for coeff_set in self.coefficients[self.statistic_name]['total_2_&coefficient']:
            big_data_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    big_data_individual_total_current_away_in_home_away_games)
            big_data_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    big_data_individual_total_opposing_teams_current_home_in_home_away_games)

            last_year_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_year_individual_total_current_away_command_in_home_away_games)
            last_year_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_year_individual_total_opposing_teams_current_home_in_home_away_games)

            similar_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    similar_command_individual_total_current_away_command_in_home_away_games)
            similar_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    similar_command_individual_total_opposing_teams_current_home_in_home_away_games)

            last_20_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_20_games_individual_total_current_away_by_year_in_home_away_games)
            last_20_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            last_12_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                        last_12_games_individual_total_current_away_by_year_in_away_games[:12])
            last_12_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                        last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games[:12])

            last_8_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_8_games_individual_total_current_away_by_year_in_home_away_games)
            last_8_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            last_4_current_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.away_structure.
                    last_4_games_individual_total_current_away_by_year_in_home_away_games)
            last_4_opposing_result = self.total_calculation(
                coeff_set=coeff_set,
                seq=self.home_structure.
                    last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

            if big_data_current_result and big_data_opposing_result:
                big_data_current_under_percent, big_data_current_over_percent = big_data_current_result
                big_data_opposing_under_percent, big_data_opposing_over_percent = big_data_opposing_result

                last_year_current_under_percent, last_year_current_over_percent = last_year_current_result
                last_year_opposing_under_percent, last_year_opposing_over_percent = last_year_opposing_result

                similar_current_under_percent, similar_current_over_percent = similar_current_result
                similar_opposing_under_percent, similar_opposing_over_percent = similar_opposing_result

                last_20_current_under_percent, last_20_current_over_percent = last_20_current_result
                last_20_opposing_under_percent, last_20_opposing_over_percent = last_20_opposing_result

                last_12_current_under_percent, last_12_current_over_percent = last_12_current_result
                last_12_opposing_under_percent, last_12_opposing_over_percent = last_12_opposing_result

                last_8_current_under_percent, last_8_current_over_percent = last_8_current_result
                last_8_opposing_under_percent, last_8_opposing_over_percent = last_8_opposing_result

                last_4_current_under_percent, last_4_current_over_percent = last_4_current_result
                last_4_opposing_under_percent, last_4_opposing_over_percent = last_4_opposing_result

                if big_data_current_under_percent and big_data_opposing_under_percent and \
                        float(coeff_set['coefficient_under']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 2 Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=68,
                                               big_data_current_percent=big_data_current_under_percent,
                                               big_data_opposing_percent=big_data_opposing_under_percent,
                                               last_year_current_percent=last_year_current_under_percent,
                                               last_year_opposing_percent=last_year_opposing_under_percent,
                                               similar_current_percent=similar_current_under_percent,
                                               similar_opposing_percent=similar_opposing_under_percent,
                                               last_20_current_percent=last_20_current_under_percent,
                                               last_20_opposing_percent=last_20_opposing_under_percent,
                                               last_12_current_percent=last_12_current_under_percent,
                                               last_12_opposing_percent=last_12_opposing_under_percent,
                                               last_8_current_percent=last_8_current_under_percent,
                                               last_8_opposing_percent=last_8_opposing_under_percent,
                                               last_4_current_percent=last_4_current_under_percent,
                                               last_4_opposing_percent=last_4_opposing_under_percent)

                if big_data_current_under_percent and big_data_opposing_under_percent and \
                        float(coeff_set['coefficient_under']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 2 Under',
                                               coeff_under_over_key='coefficient_under',
                                               ord_or_exp=85,
                                               big_data_current_percent=big_data_current_under_percent,
                                               big_data_opposing_percent=big_data_opposing_under_percent,
                                               last_year_current_percent=last_year_current_under_percent,
                                               last_year_opposing_percent=last_year_opposing_under_percent,
                                               similar_current_percent=similar_current_under_percent,
                                               similar_opposing_percent=similar_opposing_under_percent,
                                               last_20_current_percent=last_20_current_under_percent,
                                               last_20_opposing_percent=last_20_opposing_under_percent,
                                               last_12_current_percent=last_12_current_under_percent,
                                               last_12_opposing_percent=last_12_opposing_under_percent,
                                               last_8_current_percent=last_8_current_under_percent,
                                               last_8_opposing_percent=last_8_opposing_under_percent,
                                               last_4_current_percent=last_4_current_under_percent,
                                               last_4_opposing_percent=last_4_opposing_under_percent)

                if big_data_current_over_percent and big_data_opposing_over_percent and \
                        float(coeff_set['coefficient_over']) >= 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 2 Over',
                                               coeff_under_over_key='coefficient_over',
                                               ord_or_exp=68,
                                               big_data_current_percent=big_data_current_over_percent,
                                               big_data_opposing_percent=big_data_opposing_over_percent,
                                               last_year_current_percent=last_year_current_over_percent,
                                               last_year_opposing_percent=last_year_opposing_over_percent,
                                               similar_current_percent=similar_current_over_percent,
                                               similar_opposing_percent=similar_opposing_over_percent,
                                               last_20_current_percent=last_20_current_over_percent,
                                               last_20_opposing_percent=last_20_opposing_over_percent,
                                               last_12_current_percent=last_12_current_over_percent,
                                               last_12_opposing_percent=last_12_opposing_over_percent,
                                               last_8_current_percent=last_8_current_over_percent,
                                               last_8_opposing_percent=last_8_opposing_over_percent,
                                               last_4_current_percent=last_4_current_over_percent,
                                               last_4_opposing_percent=last_4_opposing_over_percent)

                if big_data_current_over_percent and big_data_opposing_over_percent and \
                        float(coeff_set['coefficient_over']) < 1.683:
                    self.is_there_a_weak_point(statistic_name=statistic_name,
                                               coeff_set=coeff_set,
                                               rate_direction='Total 2 Over',
                                               coeff_under_over_key='coefficient_over',
                                               ord_or_exp=85,
                                               big_data_current_percent=big_data_current_over_percent,
                                               big_data_opposing_percent=big_data_opposing_over_percent,
                                               last_year_current_percent=last_year_current_over_percent,
                                               last_year_opposing_percent=last_year_opposing_over_percent,
                                               similar_current_percent=similar_current_over_percent,
                                               similar_opposing_percent=similar_opposing_over_percent,
                                               last_20_current_percent=last_20_current_over_percent,
                                               last_20_opposing_percent=last_20_opposing_over_percent,
                                               last_12_current_percent=last_12_current_over_percent,
                                               last_12_opposing_percent=last_12_opposing_over_percent,
                                               last_8_current_percent=last_8_current_over_percent,
                                               last_8_opposing_percent=last_8_opposing_over_percent,
                                               last_4_current_percent=last_4_current_over_percent,
                                               last_4_opposing_percent=last_4_opposing_over_percent)
