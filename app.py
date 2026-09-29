"""
app.py
------
Main entry point for the AI Bill & Subscription Waste Detector.

Run with:
    streamlit run app.py

NOTE (Phase 1 status):
This is currently a placeholder home page so the project is runnable
from the very first phase. In later phases, the sidebar pages
(Upload, Subscriptions, Spending Analysis, Alerts, Potential Savings,
AI Insights, Settings) defined under ui/ will be wired in here.
"""

import streamlit as st

from config.config import ensure_directories, settings

# Make sure data/model/database folders exist before anything else runs.
ensure_directories()

st.set_page_config(
    page_title="AI Bill & Subscription Waste Detector",
    page_icon="💳",
    layout="wide",
)


def main() -> None:
    st.title("💳 AI Bill & Subscription Waste Detector")
    st.caption(
        "Final-year project — analyze bills and statements to spot "
        "recurring subscriptions, duplicates, price changes, and "
        "potential savings."
    )

    st.info(
        "**Project status:** Phase 1 (project structure & configuration) "
        "is complete. Upload, analysis, and dashboard pages will appear "
        "here as later phases are built.",
        icon="🚧",
    )

    with st.expander("Current configuration (from .env)", expanded=False):
        st.write(f"- **Database URL:** `{settings.DATABASE_URL}`")
        st.write(f"- **Currency symbol:** {settings.CURRENCY_SYMBOL}")
        st.write(f"- **Max upload size:** {settings.MAX_UPLOAD_SIZE_MB} MB")
        st.write(
            f"- **AI Insights enabled:** "
            f"{'Yes (API key detected)' if settings.ai_enabled else 'No (add GEMINI_API_KEY in .env to enable)'}"
        )

    st.markdown("---")
    st.subheader("What this app will do (once fully built)")
    st.markdown(
        """
- Upload CSV, Excel, PDF, or image bills/receipts
- Detect **recurring subscriptions** and explain why
- Flag **possible duplicate transactions**
- Detect **price increases** on recurring merchants
- Categorize transactions with an explainable ML model
- Visualize spending trends with interactive charts
- Simulate **potential savings** from cancelling subscriptions
- Forecast next month's approximate spending
- Answer natural-language questions about your spending (optional, via LLM)

⚠️ This project provides informational analysis only and is **not**
professional financial advice. Detections are labeled as *potential*
or *possible* findings, not certainties.
        """
    )


if __name__ == "__main__":
    main()
