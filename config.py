"""
config.py — Central configuration for the Enterprise AI Platform.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── OpenAI ─────────────────────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = "gpt-4o"

# ── Paths ──────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "sample_data")
DOCS_DIR = os.path.join(BASE_DIR, "sample_docs")

CUSTOMERS_CSV = os.path.join(DATA_DIR, "customers.csv")
TRANSACTIONS_CSV = os.path.join(DATA_DIR, "transactions.csv")

# ── Agent settings ─────────────────────────────────────────────────────────
MAX_TOKENS = 2048          # max output tokens per LLM call
CHURN_RISK_THRESHOLD = 0.5   # above this → high risk
FRAUD_AMOUNT_THRESHOLD = 2000.0
HIGH_RISK_COUNTRIES = {"RU", "CN", "NG", "KP", "IR", "BY"}
