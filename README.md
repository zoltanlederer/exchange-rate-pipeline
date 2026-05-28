# exchange-rate-pipeline

> 🚧 Work in progress

Automated ETL pipeline that fetches daily exchange rate data from the Frankfurter API, 
transforms it with pandas, and loads it into a PostgreSQL database. 
Runs on a schedule and deployed to the cloud.

## What it does

- Extracts daily EUR/USD, EUR/HUF, and EUR/GBP exchange rates from the Frankfurter API
- Seeds the database with 2 years of historical data on first run
- Transforms raw API responses into clean, typed data using pandas
- Loads the results into a PostgreSQL database
- Runs automatically on a daily schedule using APScheduler
- Deployed to Railway (cloud)

## Tech stack

- **requests** — fetching data from the Frankfurter API
- **pandas** — transforming and cleaning the data
- **psycopg2-binary** — the PostgreSQL driver, lets Python talk to PostgreSQL
- **apscheduler** — running the pipeline on a schedule
- **python-dotenv** — loading credentials from a `.env` file safely