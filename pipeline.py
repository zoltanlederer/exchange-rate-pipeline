"""ETL pipeline for fetching and storing daily exchange rate data."""

import requests
import pandas as pd
from db import get_connection

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
    
    def load(self, df):
        """Receives the DataFrame and writes each row into the PostgreSQL exchange_rates table."""
        print("Loading data...")
        conn = get_connection()
        cursor = conn.cursor()
        
        for index, row in df.iterrows(): # .iterrows() always returns two things on each iteration: the row index (0, 1, 2, 3) and the row data
            values = (row['date'], row['base_currency'], row['target_currency'], row['rate'])
            cursor.execute("INSERT INTO exchange_rates (date, base_currency, target_currency, rate) VALUES (%s, %s, %s, %s) ON CONFLICT (date, target_currency) DO NOTHING", values)

        conn.commit()
        cursor.close()
        conn.close()

    def run(self):
        """Run the full ETL pipeline — extract, transform, and load."""
        data = self.extract()
        df = self.transform(data)
        load = self.load(df)
        return load

if __name__ == '__main__':
    pipeline = ETLPipeline()
    pipeline.run()