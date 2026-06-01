"""ETL pipeline for fetching and storing daily exchange rate data."""

import requests
import pandas as pd

class ETLPipeline:
    def __init__(self):
        """Initialise the pipeline with base currency and target currencies."""
        self.currencies = ['HUF', 'GBP', 'USD', 'AUD']
        self.base_currency = 'EUR'

    def extract(self):
        """Get today's exchange rates."""
        url = f'https://api.frankfurter.app/latest?from={self.base_currency}&to={",".join(self.currencies)}'
        response = requests.get(url)
        print("Extracting data...")
        return response.json()
    
    def transform(self, data):
        """The method receives a dictionary and return a clean pandas DataFrame where each row is one currency pair."""
        print("Transforming data...")
        rows = []
        for currency, rate in data['rates'].items():
            rows.append({
                'date': data['date'],
                'base_currency': data['base'],
                'target_currency': currency,
                'rate': rate
            })
        df = pd.DataFrame(rows)
        return df

if __name__ == '__main__':
    pipeline = ETLPipeline()
    data = pipeline.extract()
    print('DATA', data)
    df = pipeline.transform(data)
    print('DF', df)