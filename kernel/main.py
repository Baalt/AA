from kernel.catchers.handicap import HandicapCatcher
from kernel.catchers.total import TotalCatcher
from kernel.catchers.total_individual import IndividualTotalCatcher
from kernel.errors import SimilarCommandError, ValidStructureError, RunError
from kernel.filters.valid import ValidStructureFilter
from kernel.structures import FromDictToStructure


class MathCore:
    def __init__(self, big_match_data: dict,
                 last_year_data: dict,
                 coefficients_data: dict,
                 all_league_data: dict,
                 league_name: str):
        self.big_match_data = big_match_data
        self.last_year_data = last_year_data
        self.coefficients_data = coefficients_data
        self.all_league_data = all_league_data
        self.league_name = league_name


class CompareStructureWithCoefficients(TotalCatcher,
                                       IndividualTotalCatcher,
                                       HandicapCatcher):
    def search(self, statistic_name: str, full_league_name: str):
        self.search_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_individual_1_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_individual_2_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_handicap_1_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_handicap_2_rate(statistic_name=statistic_name, league_name=full_league_name)


class FromHistoryToRate(MathCore, FromDictToStructure):
    def add_similar_commands_in_list(self,
                                     statistic_name,
                                     main_home_command_name,
                                     main_away_command_name):
        # print(statistic_name)
        # print(main_home_command_name)
        # print(main_away_command_name)
        command = None
        current_home_position = None
        current_away_position = None
        similar_home_commands_list = []
        similar_away_commands_list = []
        self.similar_home_commands_list = None
        self.similar_away_commands_list = None
        try:
            for command in self.all_league_data[statistic_name]:
                # print(command)
                if main_home_command_name in command or command in main_away_command_name:
                    current_home_position = int(self.all_league_data[statistic_name][command]['position'])
                elif '(' in command and command.split('(')[0].strip() in main_home_command_name:
                    current_home_position = int(self.all_league_data[statistic_name][command]['position'])

                if main_away_command_name in command or command in main_away_command_name:
                    current_away_position = int(self.all_league_data[statistic_name][command]['position'])
                elif '(' in command and command.split('(')[0].strip() in main_away_command_name:
                    current_away_position = int(self.all_league_data[statistic_name][command]['position'])

        except Exception as err:
            print(err)
            raise SimilarCommandError(f"""
    SIMILAR_COMMAND_ERROR !!!
    future/FromHistoryToRate.add_similar_commands_in_list

    HOME COMMAND NAME -- {main_home_command_name}
    AWAY COMMAND NAME -- {main_away_command_name}
    CURRENT COMMAND NAME -- {command if command else 'No commands in self.league_data[statistic_name]'}""")

        if current_home_position and current_away_position:
            for command in self.all_league_data[statistic_name]:
                try:
                    current_position = int(self.all_league_data[statistic_name][command]['position'])
                    if current_position in range(current_home_position - 3, current_home_position + 4):
                        similar_home_commands_list.append(command)
                    if current_position in range(current_away_position - 3, current_away_position + 4):
                        similar_away_commands_list.append(command)

                except IndexError:
                    return None

                except Exception as err:
                    print('FromHistoryToRate.add_similar_commands_in_list.ERROR: ', err)
                    # raise err
                    return None

        self.similar_home_commands_list = similar_home_commands_list
        self.similar_away_commands_list = similar_away_commands_list
        # print(self.similar_home_commands_list)
        # print(self.similar_away_commands_list)

    def run(self):
        main_home_command_name = self.big_match_data['home_command_name']
        main_away_command_name = self.big_match_data['away_command_name']
        for statistic_name in self.big_match_data:
            if not statistic_name.startswith('home') and not statistic_name.startswith('away'):
                try:
                    self.add_similar_commands_in_list(statistic_name=statistic_name,
                                                      main_home_command_name=main_home_command_name,
                                                      main_away_command_name=main_away_command_name)

                    if self.similar_home_commands_list and self.similar_away_commands_list:

                        home_structure = self.convert(big_match_data=self.big_match_data,
                                                      last_year_data=self.last_year_data,
                                                      statistic_name=statistic_name,
                                                      main_command_name=main_home_command_name,
                                                      home_away_collection='home_collections',
                                                      similar_home_commands_list=self.similar_home_commands_list,
                                                      similar_away_commands_list=self.similar_away_commands_list)

                        away_structure = self.convert(big_match_data=self.big_match_data,
                                                      last_year_data=self.last_year_data,
                                                      statistic_name=statistic_name,
                                                      main_command_name=main_away_command_name,
                                                      home_away_collection='away_collections',
                                                      similar_home_commands_list=self.similar_home_commands_list,
                                                      similar_away_commands_list=self.similar_away_commands_list)

                        try:
                            structures = ValidStructureFilter(home_structure=home_structure,
                                                              away_structure=away_structure)
                            structures.valid_and_create()
                            # structures.home_valid_structure_print()
                            # structures.away_valid_structure_print()
                            if structures.is_home_structure_valid() and structures.is_away_structure_valid():
                                if self.coefficients_data:
                                    compare = CompareStructureWithCoefficients(home_structure=structures.home_structure,
                                                                               away_structure=structures.away_structure,
                                                                               big_match_data=self.big_match_data,
                                                                               coefficients=self.coefficients_data,
                                                                               statistic_name=statistic_name,
                                                                               all_league_data=self.all_league_data)
                                    compare.search(statistic_name=statistic_name, full_league_name=self.league_name)

                        except ValidStructureError as err:
                            print('ValidStructureError: ', err)
                            continue

                        except KeyError as err:
                            print('FromHistoryToRate.run.ERROR: ', err)
                            continue

                        except TypeError as err:
                            print('FromHistoryToRate.run.ERROR: ', err)
                            continue

                except SimilarCommandError as err:
                    raise RunError('SimilarCommandError: ', err)


                except AttributeError as err:
                    print('FromHistoryToRate.run.ERROR: ', err)
                    continue
