import pandas as pd
from src.utils import calculate_edge

class BetScorer:
    @staticmethod
    def score(parsed_data):
        if not parsed_data: return pd.DataFrame()
        df = pd.DataFrame(parsed_data)
        
        # Group to find market average
        market_avg = df.groupby(['game', 'market', 'selection', 'point'])['odds'].mean().reset_index()
        market_avg.rename(columns={'odds': 'market_avg'}, inplace=True)
        
        df = df.merge(market_avg, on=['game', 'market', 'selection', 'point'])
        df['edge'] = df.apply(lambda x: calculate_edge(x['odds'], x['market_avg']), axis=1)
        
        # Simple Confidence (1-10)
        df['confidence'] = (df['edge'] * 2) + 5
        df['confidence'] = df['confidence'].clip(1, 10).round(1)
        
        return df.sort_values(by='edge', ascending=False)
