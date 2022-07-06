import copy
from time import sleep

from bs4 import BeautifulSoup

from browser.head import Browser
from browser.managers.coefficients import CoefficientManager
from browser.managers.league import LeagueManager
from browser.managers.match import MatchManager
from kernel.errors import NotEnoughMatchError, LiveScraperError, MatchManagerError, RunError
from kernel.filters.big_data import LastYearFilter
from kernel.main import FromHistoryToRate
from scrapers.schedule import MatchScheduleScraper

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

                except AttributeError as err:
                    print(err)
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
                # raise err
                print('FUTURE_SCRIPT_ERROR: ', err)
                continue

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
