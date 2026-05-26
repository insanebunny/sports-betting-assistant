import numpy as np

def american_to_implied_prob(american_odds):
    if american_odds > 0:
        return 100 / (american_odds + 100)
    return abs(american_odds) / (abs(american_odds) + 100)

def calculate_edge(book_odds, market_avg):
    book_prob = american_to_implied_prob(book_odds)
    market_prob = american_to_implied_prob(market_avg)
    return (market_prob - book_prob) * 100

def combine_parlay_odds(odds_list):
    decimal_odds = []
    for o in odds_list:
        if o > 0: decimal_odds.append((o/100) + 1)
        else: decimal_odds.append((100/abs(o)) + 1)
    combined = np.prod(decimal_odds)
    if combined >= 2.0: return int((combined - 1) * 100)
    return int(-100 / (combined - 1))
