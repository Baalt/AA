from bs4 import BeautifulSoup


class MatchScheduleScraper:
    def scrap_shedule_data(self, soup: BeautifulSoup) -> dict:
        schedule = {}
        league_name = None
        table_rows = soup.find('table').find_all('tr')
        for row in table_rows:
            try:
                league_name = row.find('a', attrs={'class': 'league-link'}).get_text(strip=True)
                league_url = row.find('a', attrs={'class': 'league-link'})['href']
                schedule[league_name] = {'league_url': league_url, 'match_url': []}

            except (AttributeError, TypeError):
                pass

            try:
                match_url = \
                    row.find('td', attrs={'class': 'text-right align-middle upcoming-match-prematch'}).find('a')['href']
                schedule[league_name]['match_url'].append(match_url)

            except (AttributeError, TypeError):
                pass

        return schedule
