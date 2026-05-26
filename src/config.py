import os
from dotenv import load_dotenv

load_dotenv()

ODDS_API_KEY = os.getenv('ODDS_API_KEY', '')
ODDS_API_BASE_URL = 'https://api.the-odds-api.com/v4'
DB_PATH = 'data/betting_data.db'

SPORTS_CONFIG = {
    'MLB': {'key': 'baseball_mlb', 'icon': '⚾'},
    'NBA': {'key': 'basketball_nba', 'icon': '🏀'},
    'NFL': {'key': 'americanfootball_nfl', 'icon': '🏈'},
    'Tennis': {'key': 'tennis_atp', 'icon': '🎾'}
}
