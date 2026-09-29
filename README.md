# AI Bill & Subscription Waste Detector

> **Status:** Phase 1 of 18 complete (Project structure & configuration).
> This README will be expanded into the full project documentation in a later phase.

A final-year B.Tech AI/ML project that analyzes uploaded bills and bank
statements (CSV, Excel, PDF, or images) to detect recurring subscriptions,
possible duplicate charges, price increases, and potential savings —
using classical ML (TF-IDF + Logistic Regression) plus an optional
GenAI-powered insights page.

## Folder structure (Phase 1)

```
ai_bill_waste_detector/
├── app.py                  # Streamlit entry point (placeholder home page)
├── requirements.txt
├── .env.example
├── .gitignore
├── config/
│   └── config.py           # Loads .env, exposes typed settings
├── database/                # (Phase 2: db.py, models.py, schema.sql)
├── data/
│   ├── raw/                 # Uploaded raw files land here (gitignored)
│   └── processed/           # Cleaned/normalized data (gitignored)
├── ml/
│   └── models/               # Trained model artifacts (Phase 9+)
├── services/                 # Business logic (Phase 4+)
├── ui/                       # Streamlit sub-pages (Phase 15)
├── utils/                    # Shared helpers
├── tests/                    # pytest suite
└── docs/                     # Architecture, database, API, report docs
```

## Setup (Windows / VS Code)

```bat
:: 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

:: 2. Install dependencies
pip install -r requirements.txt

:: 3. Create your local .env file from the example
copy .env.example .env

:: 4. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`. You should see a home
page confirming Phase 1 is set up correctly and showing your current
configuration.

## Environment variables

See `.env.example` for the full list. Nothing is required to get the
app running — it works out of the box with SQLite and no API key.
Add a `GEMINI_API_KEY` later (Phase 14) to enable the AI Insights page.

## What's next

Subsequent phases will add: the SQLite database layer, a synthetic
sample dataset, file parsing (CSV/Excel/PDF/OCR), data cleaning,
subscription/duplicate/price-change detection, an ML transaction
classifier, spending analytics with Plotly charts, a savings simulator,
a spending forecaster, the optional GenAI insights feature, the full
multi-page Streamlit dashboard, tests, and complete documentation.

## Disclaimer

This project is for educational purposes. It does not provide
professional financial advice, and its detections are labeled as
*potential* or *possible* findings rather than certainties.
