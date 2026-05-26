import streamlit as st
from src.odds_api import OddsAPIClient
from src.scoring import BetScorer
from src.database import DatabaseManager
from src.config import SPORTS_CONFIG

st.set_page_config(page_title="Research Assistant", layout="wide")
db = DatabaseManager()
client = OddsAPIClient()

st.title("🎯 Sports Betting Research Assistant")
st.sidebar.header("Settings")
sport_label = st.sidebar.selectbox("Sport", list(SPORTS_CONFIG.keys()))
sport_key = SPORTS_CONFIG[sport_label]['key']

if st.sidebar.button("Fetch & Analyze"):
    data = client.fetch_odds(sport_key)
    scored_df = BetScorer.score(data)
    st.session_state['data'] = scored_df
    db.save_bets(scored_df[scored_df['edge'] > 2])

if 'data' in st.session_state:
    df = st.session_state['data']
    t1, t2, t3 = st.tabs(["🔥 Top Picks", "🚫 Avoid", "🕒 History"])
    
    with t1:
        st.dataframe(df[df['edge'] > 0], use_container_width=True)
    with t2:
        st.dataframe(df[df['edge'] < -2], use_container_width=True)
    with t3:
        st.dataframe(db.get_history(), use_container_width=True)
else:
    st.info("Click 'Fetch & Analyze' to load live market data.")
