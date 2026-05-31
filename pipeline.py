"""ETL pipeline for fetching and storing daily exchange rate data."""

import requests

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

if __name__ == '__main__':
    pipeline = ETLPipeline()
    data = pipeline.extract()
    print(data)