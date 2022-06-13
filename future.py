import copy
import pickle
from pprint import pprint
from time import sleep
from bs4 import BeautifulSoup

from scrapers.schedule import MatchScheduleScraper
from browser.head import Browser
from browser.managers.match import MatchManager
from browser.managers.league import LeagueManager
from browser.managers.coefficients import CoefficientManager
from kernel.filters.big_data import LastYearFilter
from kernel.filters.valid import ValidStructureFilter
from kernel.structures import FromDictToStructure
from kernel.catchers.total import TotalCatcher
from kernel.catchers.total_individual import IndividualTotalCatcher
from kernel.catchers.handicap import HandicapCatcher
from kernel.errors import SimilarCommandError, RunError, LiveScraperError, NotEnoughMatchError, MatchManagerError, \
    ValidStructureError


class CompareStructureWithCoefficients(TotalCatcher,
                                       IndividualTotalCatcher,
                                       HandicapCatcher):
    def search(self, statistic_name: str):
        self.search_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_individual_1_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_individual_2_total_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_handicap_1_rate(statistic_name=statistic_name, league_name=full_league_name)
        self.search_handicap_2_rate(statistic_name=statistic_name, league_name=full_league_name)


class MathCore:
    def __init__(self, big_match_data: dict,
                 last_year_data: dict,
                 coefficients_data: dict,
                 all_league_data: dict,
                 league_name: str):
        self.big_match_data = big_match_data
        self.last_year_data = last_year_data
        self.coefficients_data = coefficients_data
        self.league_data = all_league_data
        self.league_name = league_name


class FromHistoryToRate(MathCore, FromDictToStructure):
    def add_similar_commands_in_list(self,
                                     statistic_name,
                                     main_home_command_name,
                                     main_away_command_name):
        command = None
        current_home_position = None
        current_away_position = None
        similar_home_commands_list = []
        similar_away_commands_list = []
        self.similar_home_commands_list = None
        self.similar_away_commands_list = None
        try:

            for command in self.league_data[statistic_name]:
                if main_home_command_name in command or command in main_away_command_name:
                    current_home_position = int(self.league_data[statistic_name][command]['position'])
                elif '(' in command and command.split('(')[0].strip() in main_home_command_name:
                    current_home_position = int(self.league_data[statistic_name][command]['position'])

                if main_away_command_name in command or command in main_away_command_name:
                    current_away_position = int(self.league_data[statistic_name][command]['position'])
                elif '(' in command and command.split('(')[0].strip() in main_away_command_name:
                    current_away_position = int(self.league_data[statistic_name][command]['position'])

        except Exception as err:
            print(err)
            raise SimilarCommandError(f"""
    SIMILAR_COMMAND_ERROR !!!
    future/FromHistoryToRate.add_similar_commands_in_list
            
    HOME COMMAND NAME -- {main_home_command_name}
    AWAY COMMAND NAME -- {main_away_command_name}
    CURRENT COMMAND NAME -- {command if command else 'No commands in self.league_data[statistic_name]'}""")

        if current_home_position and current_away_position:
            for command in self.league_data[statistic_name]:
                try:
                    current_position = int(self.league_data[statistic_name][command]['position'])
                    if current_position in range(current_home_position - 3, current_home_position + 4):
                        similar_home_commands_list.append(command)
                    if current_position in range(current_away_position - 3, current_away_position + 4):
                        similar_away_commands_list.append(command)

                except IndexError:
                    return None

                except Exception as err:
                    print('FromHistoryToRate.add_similar_commands_in_list.ERROR: ', err)
                    return None

        self.similar_home_commands_list = similar_home_commands_list
        self.similar_away_commands_list = similar_away_commands_list

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
                            if structures.is_home_structure_valid() and structures.is_away_structure_valid():
                                if self.coefficients_data:
                                    compare = CompareStructureWithCoefficients(home_structure=structures.home_structure,
                                                                               away_structure=structures.away_structure,
                                                                               big_match_data=self.big_match_data,
                                                                               coefficients=self.coefficients_data,
                                                                               statistic_name=statistic_name)
                                    compare.search(statistic_name=statistic_name)

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


if __name__ == '__main__':
    all_live_data = {}
    browser = Browser()
    browser.login()
    sleep(1)
    input('Choose the day and press "Enter".')
    soup = BeautifulSoup(browser.get_html, 'lxml')
    football_schedule_data: dict = MatchScheduleScraper().scrap_shedule_data(soup=soup)
    for full_league_name in football_schedule_data:
        if 'Brazil: Serie B' in full_league_name:
            continue
        if ':' in full_league_name:
            if 'Norway: Division 1' in full_league_name:
                league = full_league_name.split(':')[-1].strip()
                browser.open_new_page(football_schedule_data[full_league_name]['league_url'])
                sleep(1)
                soup = BeautifulSoup(browser.get_html, 'lxml')
                all_league_data = LeagueManager(browser=browser, soup=soup).get_data
                for match in football_schedule_data[full_league_name]['match_url']:
                    try:
                        browser.open_new_page(match)
                        sleep(1)

                        try:
                            match_manager = MatchManager(browser, league=league, all_live_data=all_live_data)

                        except (NotEnoughMatchError, LiveScraperError, MatchManagerError) as err:
                            print(err)
                            continue

                        except AttributeError:
                            continue

                        match_manager.filter_out(number_of_matches=100)
                        sleep(1)
                        soup = BeautifulSoup(browser.get_html, 'lxml')
                        is_match_data = match_manager.get_match_data(soup=soup)

                        if is_match_data:
                            sleep(1)
                            copy_match_data = copy.deepcopy(match_manager.get_data)

                            coeff_manager = CoefficientManager(browser=browser)
                            coeff_manager.get_coefficients_data()
                            sleep(1)

                            last_year_data = LastYearFilter(all_match_data=copy_match_data, all_referee_data=None)
                            last_year_data.filter_home_away_collections('home_collections')
                            last_year_data.filter_home_away_collections('away_collections')
                            # last_year_data.filter_referee_collections()

                            math_collector = FromHistoryToRate(big_match_data=match_manager.get_data,
                                                               last_year_data=last_year_data.all_match_data,
                                                               coefficients_data=coeff_manager.get_data,
                                                               all_league_data=all_league_data,
                                                               league_name=full_league_name)
                            math_collector.run()

                    except RunError as err:
                        print('RunError: ', err)
                        continue

                    except Exception as err:
                        raise err
                        # print('MAIN_SCRIPT_ERROR: ', err)
                        # continue

    print('Search is over.')
    #
    # for match in all_live_data.copy():
    #     if not all_live_data[match]:
    #         del all_live_data[match]
    #
    # pprint(all_live_data)
    # live_data_file = open('livedata.pkl', 'wb')
    # pickle.dump(all_live_data, live_data_file)
    # live_data_file.close()
    #
    # live_data_file = open('livedata.pkl', 'rb')
    # output = pickle.load(live_data_file)
    # pprint(output)
    # print('Search is over.')
    # # browser.close()
    # referee = RefereeManager(browser=browser, league='Serie A')
    # try:
    #     referee.get_referee_data()
    #     copy_referee_data = copy.deepcopy(referee.get_data) if referee.get_data else None
    #
    #
    # except Exception:
    #     copy_referee_data = None
