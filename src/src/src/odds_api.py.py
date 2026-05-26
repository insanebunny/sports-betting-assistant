import requests
import streamlit as st
from src.config import ODDS_API_KEY, ODDS_API_BASE_URL

class OddsAPIClient:
    def __init__(self):
        self.key = ODDS_API_KEY

    def fetch_odds(self, sport_key, markets='h2h,spreads,totals'):
        url = f"{ODDS_API_BASE_URL}/sports/{sport_key}/odds"
        params = {'apiKey': self.key, 'regions': 'us', 'markets': markets, 'oddsFormat': 'american'}
        res = requests.get(url, params=params)
        if res.status_code != 200: return []
        
        parsed = []
        for event in res.json():
            for book in event.get('bookmakers', []):
                for mkt in book.get('markets', []):
                    for outcome in mkt.get('outcomes', []):
                        parsed.append({
                            'game': f"{event['away_team']} @ {event['home_team']}",
                            'sport': sport_key,
                            'market': mkt['key'],
                            'selection': outcome['name'],
                            'point': outcome.get('point'),
                            'book': book['title'],
                            'odds': outcome['price']
                        })
        return parsed
