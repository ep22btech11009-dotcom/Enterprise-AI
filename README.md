# Enterprise AI Analytics Platform

A production-ready multi-agent AI pipeline with RAG, ML models, and ROI quantification.
Built with OpenAI GPT-4o + LlamaIndex + scikit-learn.

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────────────┐
│   Supervisor Agent          │  ← GPT-4o with function calling; plans & routes tasks
└──────────┬──────────────────┘
           │
    ┌──────┴───────┬────────────┬──────────────┐
    ▼              ▼            ▼              ▼
DataAgent    AnalysisAgent   MLAgent      RAGEngine
(CSV/SQL)    (stats/anomaly) (churn/fraud) (LlamaIndex + OpenAI)
    │              │            │              │
    └──────────────┴────────────┴──────────────┘
                        │
                        ▼
                   ROI Agent
              (revenue/risk/savings)
                        │
                        ▼
                  Insight Agent
              (GPT-4o narrative)
                        │
                        ▼
               Final Business Insight
```

---

## Quick Start

### 1. Unzip and open in VS Code

```bash
cd enterprise_ai_platform
code .
```

### 2. Create a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

```bash
cp .env.example .env
# Open .env and paste your key:
# OPENAI_API_KEY=sk-...
```

Get your key at: https://platform.openai.com/api-keys

### 5. Run

```bash
# Run all 3 demo queries
python main.py

# Run a custom query
python main.py --query "What is our current MRR and which customers are at risk?"

# Skip RAG (no OpenAI embedding calls, faster for testing)
python main.py --no-rag
```

---

## Project Structure

```
enterprise_ai_platform/
├── main.py                   # CLI entry point
├── config.py                 # API key, model, thresholds, paths
├── requirements.txt
├── .env.example              # Copy to .env and add your key
│
├── agents/
│   ├── supervisor.py         # Orchestrator — GPT-4o function calling
│   ├── data_agent.py         # CSV/SQL data loading & queries
│   ├── analysis_agent.py     # Anomaly detection, trend, forecast
│   ├── ml_agent.py           # Churn (Random Forest) + fraud (Isolation Forest)
│   ├── roi_agent.py          # Revenue / cost / risk quantification
│   └── insight_agent.py      # Final narrative synthesis (GPT-4o)
│
├── rag/
│   └── rag_engine.py         # LlamaIndex + OpenAI embeddings
│
├── sample_data/
│   ├── customers.csv         # 15 sample customers with churn labels
│   └── transactions.csv      # 20 sample transactions (3 flagged)
│
└── sample_docs/
    ├── fraud_sop.txt         # Fraud detection SOP (indexed by RAG)
    └── churn_policy.txt      # Churn retention policy (indexed by RAG)
```

---

## Models Used

| Component | Model |
|---|---|
| Supervisor (orchestration) | `gpt-4o` via function calling |
| Insight Agent (narrative) | `gpt-4o` |
| ROI Agent (narrative) | `gpt-4o` |
| RAG LLM | `gpt-4o` via LlamaIndex |
| RAG Embeddings | `text-embedding-3-small` |
| Churn Model | `RandomForestClassifier` (scikit-learn) |
| Fraud Model | `IsolationForest` (scikit-learn) |

---

## Demo Queries

The default run executes three queries end-to-end:

1. **Churn Risk** — "Which customers have the highest churn risk and what is the revenue at stake?"
2. **Fraud Detection** — "Detect anomalies in our transactions per our fraud policy."
3. **Revenue Forecast + ROI** — "Forecast revenue for 3 months and show the ROI of a retention campaign."

---

## Extending the Platform

| Goal | Where to edit |
|---|---|
| Add a new data source | `agents/data_agent.py` |
| Add a new ML model | `agents/ml_agent.py` |
| Add documents to RAG | Drop `.txt` / `.pdf` files in `sample_docs/` |
| Add a new agent tool | `agents/supervisor.py` → `TOOLS` list + `_execute_tool()` |
| Switch to a different model | `config.py` → `MODEL` |

---

## Troubleshooting

**`ModuleNotFoundError: openai`**
→ Run `pip install -r requirements.txt` inside your activated venv.

**`AuthenticationError`**
→ Check your `.env` has the correct `OPENAI_API_KEY=sk-...`

**RAG slow on first run**
→ OpenAI embeddings are called per document chunk on first index build. This is normal.
→ Use `python main.py --no-rag` to skip RAG during development.

**Windows path issues**
→ Use `venv\Scripts\activate` instead of `source venv/bin/activate`.
