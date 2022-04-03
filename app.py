from bs4 import BeautifulSoup

from browser.head import Browser
from browser.managers import LeagueManager
from scraper.directions import MatchScheduleScraper, LeagueScraper

if __name__ == '__main__':
    browser = Browser()
    input('Chose game day for rate searching and after click "Enter"')
    soup = BeautifulSoup(browser.get_html, 'lxml')
    football_match_data: dict = MatchScheduleScraper().scrap_football_matches_urls(soup)
    print(football_match_data)
    browser.open_new_page('/league/England/Premier_League')
    soup = BeautifulSoup(browser.get_html, 'lxml')
    all_league_data = LeagueManager(browser, soup).get_league_data()